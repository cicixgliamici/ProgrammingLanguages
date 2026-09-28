$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$failures = [System.Collections.Generic.List[string]]::new()
$skipped = [System.Collections.Generic.List[string]]::new()

function Test-Tool {
    param([Parameter(Mandatory)][string]$Name)

    return $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

function Invoke-Check {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][scriptblock]$Action
    )

    Write-Host "`n== $Name ==" -ForegroundColor Cyan
    try {
        & $Action
        if ($LASTEXITCODE -ne 0) {
            throw "$Name exited with code $LASTEXITCODE."
        }
        Write-Host "PASS: $Name" -ForegroundColor Green
    }
    catch {
        $failures.Add("${Name}: $($_.Exception.Message)")
        Write-Host "FAIL: $Name" -ForegroundColor Red
    }
}

function Add-SkippedCheck {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Reason
    )

    $skipped.Add("${Name}: $Reason")
    Write-Host "SKIP: $Name - $Reason" -ForegroundColor Yellow
}

Push-Location $repositoryRoot
try {
    if (Test-Tool "cmake") {
        Invoke-Check "C configuration" { cmake -S C -B build/c }
        Invoke-Check "C compilation" { cmake --build build/c }
        Invoke-Check "C smoke tests" { ctest --test-dir build/c --output-on-failure }
    }
    else {
        Add-SkippedCheck "C" "CMake is not installed."
    }

    if (Test-Tool "mvn") {
        Invoke-Check "Java compilation and tests" { mvn -q -f Java/pom.xml test }
        Invoke-Check "Spring Boot compilation and tests" { mvn -q -f Spring/ProductExample/pom.xml test }
    }
    else {
        Add-SkippedCheck "Java and Spring Boot" "Maven is not installed."
    }

    if (Test-Tool "sbt") {
        Invoke-Check "Scala compilation" {
            Push-Location Scala
            try {
                sbt --batch --no-colors compile
            }
            finally {
                Pop-Location
            }
        }
    }
    else {
        Add-SkippedCheck "Scala" "sbt is not installed."
    }

    if (Test-Tool "python") {
        Invoke-Check "Python tests" { python -m unittest discover -s Python/tests -v }
    }
    else {
        Add-SkippedCheck "Python" "Python is not installed."
    }

    $leanToolchainInstalled = (Test-Tool "elan") -and
        ((elan toolchain list) -match "leanprover/lean4:v4.19.0")
    if ((Test-Tool "lean") -and $leanToolchainInstalled) {
        Invoke-Check "Lean lessons" {
            foreach ($leanFile in (Get-ChildItem Lean -Filter *.lean | Sort-Object Name)) {
                lean $leanFile.FullName
                if ($LASTEXITCODE -ne 0) {
                    throw "Lean verification failed for $($leanFile.Name)."
                }
            }
        }
    }
    else {
        Add-SkippedCheck "Lean" "The pinned Lean v4.19.0 toolchain is not installed."
    }

    if (Test-Tool "coqc") {
        Invoke-Check "Coq lessons" {
            foreach ($coqFile in (Get-Content _CoqProject | Where-Object { $_ -and -not $_.StartsWith("#") })) {
                coqc $coqFile
                if ($LASTEXITCODE -ne 0) {
                    throw "Coq verification failed for $coqFile."
                }
            }
        }
    }
    else {
        Add-SkippedCheck "Coq" "coqc is not installed."
    }
}
finally {
    Pop-Location
}

Write-Host "`nVerification summary" -ForegroundColor Cyan
$skipped | ForEach-Object { Write-Host "SKIPPED: $_" -ForegroundColor Yellow }
$failures | ForEach-Object { Write-Host "FAILED: $_" -ForegroundColor Red }

if ($failures.Count -gt 0) {
    exit 1
}

Write-Host "All available checks passed." -ForegroundColor Green
