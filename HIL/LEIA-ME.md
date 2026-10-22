# Preparação do ambiente HIL — 21/10/2026

## Instalado

- ambiente Python isolado em `ambiente_python`;
- NumPy, SciPy, Matplotlib e pySerial;
- extensão PlatformIO IDE no VS Code;
- PlatformIO Core 6.2.0 e plataforma Espressif 32 8.0.0;
- o computador já possuía Python 3.14, Git, VS Code, MATLAB R2017a e o pacote ESP32 do Arduino.

## Projeto inicial

`esp32_hil_base` contém um firmware para ESP32 DevKit V1 de 30 pinos e um modelo de planta no PC. O firmware foi gravado e testado fisicamente pela porta COM5 em 21/10/2026.

## Verificações concluídas

- simulação numérica comparada com a solução analítica: aprovada;
- comunicação serial virtual em loopback: aprovada;
- execução offline da planta e do controlador: aprovada;
- compilação do firmware para `esp32doit-devkit-v1`: aprovada;
- gravação e verificação do firmware no ESP32-D0WD-V3: aprovadas;
- comunicação USB serial a 921.600 bit/s: aprovada;
- ensaio HIL com 1000 ciclos e período de 10 ms: aprovado, sem falhas de sequência ou violações de prazo;
- uso da compilação: 22.132 bytes de RAM (6,8%) e 307.796 bytes de flash da partição de programa (23,5%).

As portas COM3 e COM4 pertencem ao Bluetooth. O ESP32 conectado por um conversor USB CH9102 foi identificado como COM5.

## Resultado do ensaio físico

O ensaio final durou 10,0009 s e apresentou latência média de 3,5510 ms, percentil 95 de 4,1618 ms e máxima de 4,8782 ms. A saída da planta atingiu 90% da referência em 310 ms de tempo nominal e convergiu para 1,000000 sem sobressinal observado.

O relatório completo, o CSV e o gráfico estão na pasta [`esp32_hil_base/resultados`](esp32_hil_base/resultados).

## Limites desta preparação

O ensaio confirma o funcionamento desta configuração específica, mas não demonstra comportamento de tempo real determinístico nem estabelece um limite de pior caso. O período inicial recomendado neste computador é 10 ms; períodos menores exigem novos testes e podem demandar outra interface ou estratégia de comunicação.

