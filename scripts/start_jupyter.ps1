Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

$env:JUPYTER_CONFIG_DIR = Join-Path $ProjectRoot ".jupyter\config"
$env:JUPYTER_DATA_DIR = Join-Path $ProjectRoot ".jupyter\data"
$env:JUPYTER_RUNTIME_DIR = Join-Path $ProjectRoot ".jupyter\runtime"
$env:IPYTHONDIR = Join-Path $ProjectRoot ".ipython"

New-Item -ItemType Directory -Force -Path $env:JUPYTER_CONFIG_DIR, $env:JUPYTER_DATA_DIR, $env:JUPYTER_RUNTIME_DIR, $env:IPYTHONDIR | Out-Null

$KernelDir = Join-Path $env:JUPYTER_DATA_DIR "kernels\ab-testing"
New-Item -ItemType Directory -Force -Path $KernelDir | Out-Null
$KernelSpec = @{
    argv = @(
        (Join-Path $ProjectRoot ".venv\Scripts\python.exe"),
        "-m",
        "ipykernel_launcher",
        "-f",
        "{connection_file}"
    )
    display_name = "Python (ab-testing)"
    language = "python"
} | ConvertTo-Json -Depth 4
$KernelPath = Join-Path $KernelDir "kernel.json"
[System.IO.File]::WriteAllText($KernelPath, $KernelSpec, [System.Text.UTF8Encoding]::new($false))

& "$ProjectRoot\.venv\Scripts\jupyter-lab.exe" --notebook-dir "$ProjectRoot"
