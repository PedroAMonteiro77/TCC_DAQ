# Preparação do ambiente HIL — 21/10/2026

## Instalado

- ambiente Python isolado em `ambiente_python`;
- NumPy, SciPy, Matplotlib e pySerial;
- extensão PlatformIO IDE no VS Code;
- PlatformIO Core 6.2.0 e plataforma Espressif 32 8.0.0;
- o computador já possuía Python 3.14, Git, VS Code, MATLAB R2017a e o pacote ESP32 do Arduino.

## Projeto inicial

`esp32_hil_base` contém um firmware para ESP32 DevKit V1 de 30 pinos e um modelo de planta no PC. O firmware ainda não foi gravado na placa.

## Verificações concluídas

- simulação numérica comparada com a solução analítica: aprovada;
- comunicação serial virtual em loopback: aprovada;
- execução offline da planta e do controlador: aprovada;
- compilação do firmware para `esp32doit-devkit-v1`: aprovada;
- uso da compilação: 22.132 bytes de RAM (6,8%) e 307.592 bytes de flash da partição de programa (23,5%).

As portas COM3 e COM4 encontradas pertencem ao Bluetooth. Nenhuma porta USB do ESP32 estava disponível durante a verificação.

## Limites desta preparação

O teste offline valida as bibliotecas e o modelo básico. Ele não valida driver USB, porta COM, cabo, firmware, latência da comunicação nem operação em tempo real. Essas verificações serão feitas com a placa conectada.

