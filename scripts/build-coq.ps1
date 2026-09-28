[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$projectFile = Join-Path $repositoryRoot "config/coq/_CoqProject"
$buildDirectory = Join-Path $repositoryRoot "build/coq"
$makefile = Join-Path $buildDirectory "CoqMakefile"

# Coq source paths in _CoqProject are relative to the repository root.
New-Item -ItemType Directory -Force -Path $buildDirectory | Out-Null
Push-Location $repositoryRoot
try {
    coq_makefile -f $projectFile -o $makefile
    if ($LASTEXITCODE -ne 0) {
        throw "coq_makefile exited with code $LASTEXITCODE."
    }

    make -f $makefile
    if ($LASTEXITCODE -ne 0) {
        throw "Coq build exited with code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
