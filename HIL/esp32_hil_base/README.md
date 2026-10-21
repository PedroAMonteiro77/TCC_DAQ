# Ambiente inicial de HIL com ESP32 DevKit V1

Arquitetura do primeiro ensaio:

1. o PC executa uma planta de primeira ordem;
2. o ESP32 executa um controlador PI;
3. PC e ESP32 trocam medição e controle por USB serial;
4. o script registra a resposta e a latência observada.

O teste em `--modo simulado` verifica o software do PC sem depender da placa. O modo serial exige compilar e gravar o firmware com PlatformIO.

## VS Code e PlatformIO

Abra esta pasta no VS Code. A configuração usa a placa `esp32doit-devkit-v1`, o framework Arduino e 921600 bit/s. Use **PlatformIO: Build** para compilar e **PlatformIO: Upload** para gravar. A gravação substitui o firmware atualmente presente na placa.

## Ambiente Python

No PowerShell, a partir desta pasta:

```powershell
..\ambiente_python\Scripts\python.exe hil_pc.py --modo simulado
```

Como atalho, também é possível executar `executar_teste_offline.ps1`. Para recompilar o firmware pela linha de comando, use `compilar_firmware.ps1`.

Após conectar e gravar o ESP32, descubra a porta COM e execute, por exemplo:

```powershell
..\ambiente_python\Scripts\python.exe hil_pc.py --modo serial --porta COM5
```

Os arquivos do ensaio são gravados em `resultados`. O Windows e a comunicação USB serial não oferecem garantia automática de tempo real; período, latência, jitter e perdas devem ser medidos na configuração usada.

