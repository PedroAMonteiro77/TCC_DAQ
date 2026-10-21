$ErrorActionPreference = 'Stop'
$pythonHil = Join-Path $PSScriptRoot '..\ambiente_python\Scripts\python.exe'
& $pythonHil -m platformio run --project-dir $PSScriptRoot
if ($LASTEXITCODE -ne 0) { throw 'A compilação falhou.' }

