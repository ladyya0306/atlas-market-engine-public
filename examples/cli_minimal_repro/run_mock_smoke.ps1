param(
    [int]$Rounds = 1,
    [int]$Seed = 42
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path))
Set-Location $Root
python scripts/public_smoke_test.py --rounds $Rounds --seed $Seed
