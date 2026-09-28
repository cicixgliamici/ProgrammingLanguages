[CmdletBinding()]
param(
    [switch]$RequireAll
)

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
        Invoke-Check "C tests" { ctest --test-dir build/c --output-on-failure }
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
        Invoke-Check "Scala compilation and tests" {
            Push-Location Scala
            try {
                sbt --batch --no-colors test
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

        python -c "import numpy" 2>$null
        if ($LASTEXITCODE -eq 0) {
            if ($RequireAll) {
                Invoke-Check "Pinned NumPy version" {
                    $requirement = Get-Content Python/requirements/numpy.txt |
                        Where-Object { $_ -match "^numpy==" } |
                        Select-Object -First 1
                    $expectedVersion = $requirement.Split("==")[1]
                    $installedVersion = (python -c "import numpy; print(numpy.__version__)").Trim()
                    if ($installedVersion -ne $expectedVersion) {
                        throw "Expected NumPy $expectedVersion, found $installedVersion."
                    }
                }
            }

            Invoke-Check "NumPy lessons" {
                foreach ($numpyFile in (Get-ChildItem Python/numpy -Filter *.py | Sort-Object Name)) {
                    python $numpyFile.FullName
                    if ($LASTEXITCODE -ne 0) {
                        throw "NumPy verification failed for $($numpyFile.Name)."
                    }
                }
            }
        }
        else {
            Add-SkippedCheck "NumPy lessons" "Install Python/requirements/numpy.txt."
        }
    }
    else {
        Add-SkippedCheck "Python" "Python is not installed."
    }

    if (Test-Tool "lake") {
        Invoke-Check "Lean Lake project" { lake build }
    }
    else {
        Add-SkippedCheck "Lean" "Lake is not installed; lean-toolchain pins the required version."
    }

    if (Test-Tool "coqc") {
        Invoke-Check "Coq lessons" {
            $coqFiles = Get-Content _CoqProject |
                Where-Object { $_ -and -not $_.StartsWith("#") -and -not $_.StartsWith("-") }
            foreach ($coqFile in $coqFiles) {
                coqc -Q Coq LearningCoq $coqFile
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

if ($RequireAll -and $skipped.Count -gt 0) {
    Write-Host "Strict verification requires every toolchain." -ForegroundColor Red
    exit 2
}

if ($skipped.Count -gt 0) {
    Write-Host "All available checks passed; some toolchains were skipped." -ForegroundColor Green
}
else {
    Write-Host "All checks passed." -ForegroundColor Green
}
