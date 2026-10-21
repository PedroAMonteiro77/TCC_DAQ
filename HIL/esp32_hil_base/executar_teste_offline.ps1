$ErrorActionPreference = 'Stop'
$pythonHil = Join-Path $PSScriptRoot '..\ambiente_python\Scripts\python.exe'
& $pythonHil (Join-Path $PSScriptRoot 'hil_pc.py') --modo simulado
if ($LASTEXITCODE -ne 0) { throw 'O teste offline falhou.' }

