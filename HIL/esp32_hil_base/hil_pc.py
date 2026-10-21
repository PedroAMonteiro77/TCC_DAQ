"""Primeiro ensaio HIL: planta no PC e controlador no ESP32.

Sem placa: python hil_pc.py --modo simulado
Com placa: python hil_pc.py --modo serial --porta COMx
"""
from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import serial


def controller_simulated(y: float, integral: float, dt: float) -> tuple[float, float]:
    error = 1.0 - y
    integral = np.clip(integral + 8.0 * dt * error, 0.0, 3.3)
    u = float(np.clip(1.2 * error + integral, 0.0, 3.3))
    return u, float(integral)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--modo', choices=('simulado', 'serial'), default='simulado')
    parser.add_argument('--porta', help='Exemplo: COM5')
    parser.add_argument('--passos', type=int, default=2000)
    parser.add_argument('--periodo-ms', type=float, default=1.0)
    args = parser.parse_args()
    if args.modo == 'serial' and not args.porta:
        parser.error('--porta e obrigatoria no modo serial')

    dt = args.periodo_ms / 1000.0
    y = 0.0
    integral = 0.0
    rows: list[tuple[int, float, float, float, float]] = []
    port = serial.Serial(args.porta, 921600, timeout=0.2) if args.modo == 'serial' else None
    if port:
        time.sleep(2.0)
        port.reset_input_buffer()

    deadline = time.perf_counter()
    try:
        for sequence in range(args.passos):
            start = time.perf_counter()
            if port:
                port.write(f'MEAS,{sequence},{y:.7f}\n'.encode('ascii'))
                response = port.readline().decode('ascii', errors='replace').strip()
                fields = response.split(',')
                if len(fields) != 4 or fields[0] != 'CTRL' or int(fields[1]) != sequence:
                    raise RuntimeError(f'Resposta inesperada: {response!r}')
                u = float(fields[2])
            else:
                u, integral = controller_simulated(y, integral, dt)

            # Planta ilustrativa: dy/dt=(-y+u)/0,1, integrada por Euler.
            y += dt * (-y + u) / 0.1
            elapsed = time.perf_counter() - start
            rows.append((sequence, sequence * dt, y, u, elapsed))
            if port:
                deadline += dt
                remaining = deadline - time.perf_counter()
                if remaining > 0:
                    time.sleep(remaining)
    finally:
        if port:
            port.close()

    result = Path(__file__).resolve().parent / 'resultados'
    result.mkdir(exist_ok=True)
    with (result / 'ensaio.csv').open('w', newline='', encoding='utf-8') as stream:
        writer = csv.writer(stream)
        writer.writerow(('sequencia', 'tempo_s', 'y', 'u', 'latencia_s'))
        writer.writerows(rows)

    data = np.asarray(rows)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
    ax1.plot(data[:, 1], data[:, 2], label='Saida da planta')
    ax1.axhline(1.0, color='k', linestyle='--', label='Referencia')
    ax1.set_ylabel('Amplitude')
    ax1.legend()
    ax1.grid(alpha=0.3)
    ax2.plot(data[:, 1], data[:, 4] * 1e3)
    ax2.axhline(args.periodo_ms, color='r', linestyle='--', label='Periodo solicitado')
    ax2.set(xlabel='Tempo (s)', ylabel='Latencia por ciclo (ms)')
    ax2.legend()
    ax2.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(result / 'ensaio.png', dpi=160)
    print(f'Modo: {args.modo}; passos: {args.passos}; y final: {y:.6f}')
    print(f'Latencia maxima observada: {data[:, 4].max() * 1e3:.3f} ms')
    print('Este ensaio mede a configuracao testada; nao prova um limite de pior caso.')


if __name__ == '__main__':
    main()

