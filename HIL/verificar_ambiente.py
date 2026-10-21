"""Verifica o ambiente no PC; nao grava nem abre uma placa conectada."""
from pathlib import Path
import json
import platform
import numpy as np
import scipy
from scipy.signal import cont2discrete
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import serial
from serial.tools import list_ports

root = Path(__file__).resolve().parent
out = root / 'resultados_verificacao'
out.mkdir(exist_ok=True)

# Modelo ilustrativo: G(s)=1/(0,1s+1). Simulacao offline, sem prazo real.
dt = 0.001
a, b, c, d, _ = cont2discrete((
    np.array([[-10.0]]),
    np.array([[10.0]]),
    np.array([[1.0]]),
    np.array([[0.0]]),
), dt)
t = np.arange(0, 1.001, dt)
y = np.zeros(t.size)
for k in range(1, t.size):
    y[k] = a[0, 0] * y[k-1] + b[0, 0]
expected = 1 - np.exp(-10*t)
np.testing.assert_allclose(y, expected, atol=1e-12)

# Loopback virtual: testa a biblioteca, nao USB, ESP32 ou seus drivers.
with serial.serial_for_url('loop://', timeout=1) as port:
    payload = b'HIL-PC-CHECK\n'
    port.write(payload)
    if port.read(len(payload)) != payload:
        raise RuntimeError('Falha no loopback serial virtual')

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, y)
ax.set(xlabel='Tempo simulado (s)', ylabel='Saida normalizada',
       title='Verificacao do ambiente: simulacao offline de primeira ordem')
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(out/'simulacao_offline.png', dpi=160)
plt.close(fig)
report = {
    'python': platform.python_version(),
    'numpy': np.__version__, 'scipy': scipy.__version__,
    'matplotlib': matplotlib.__version__, 'pyserial': serial.__version__,
    'simulacao_offline': 'aprovada: comparacao com solucao analitica',
    'serial_loopback_virtual': 'aprovado',
    'portas_disponiveis': [{'porta': p.device, 'descricao': p.description} for p in list_ports.comports()],
    'hardware_testado': False,
    'tempo_real_validado': False,
}
(out/'diagnostico.json').write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(report, indent=2, ensure_ascii=False))
