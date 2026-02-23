# MotoCoop - Start Dev
# Uso: .\start-dev.ps1
# Após executar, use comandos normalmente: python, uvicorn, pytest, etc

$venvPath = "C:\Users\Jonathan\AppData\Local\pypoetry\Cache\virtualenvs\motocoop-9ldtuIyD-py3.11\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    & $venvPath
    Write-Host "✅ Ambiente Python 3.11 ativado!" -ForegroundColor Green
    Write-Host "🐍 Python: $(python --version)" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host "❌ Ambiente virtual não encontrado!" -ForegroundColor Red
    Write-Host "Execute: poetry install" -ForegroundColor Yellow
}


