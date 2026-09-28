[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$configurationDirectory = Join-Path $repositoryRoot "config/lean"

# Running Lake from its configuration directory keeps generated state away
# from the repository root while srcDir still points at the lesson sources.
Push-Location $configurationDirectory
try {
    lake build
    if ($LASTEXITCODE -ne 0) {
        throw "Lake build exited with code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
