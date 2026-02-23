# MotoCoop - Verificar Configuração
# Uso: .\check-setup.ps1

Write-Host "`n=== Verificando Configuração ===" -ForegroundColor Cyan

# Verificar Python 3.11
Write-Host "`n1. Verificando Python 3.11..." -ForegroundColor Yellow
$python311 = "C:\Users\Jonathan\AppData\Local\Programs\Python\Python311\python.exe"
if (Test-Path $python311) {
    Write-Host "   ✅ Python 3.11 instalado" -ForegroundColor Green
    & $python311 --version
} else {
    Write-Host "   ❌ Python 3.11 não encontrado" -ForegroundColor Red
}

# Verificar ambiente virtual Poetry
Write-Host "`n2. Verificando ambiente virtual..." -ForegroundColor Yellow
$venv = "C:\Users\Jonathan\AppData\Local\pypoetry\Cache\virtualenvs\motocoop-9ldtuIyD-py3.11"
if (Test-Path $venv) {
    Write-Host "   ✅ Ambiente virtual criado" -ForegroundColor Green
} else {
    Write-Host "   ❌ Ambiente virtual não encontrado" -ForegroundColor Red
}

# Testar ativação
Write-Host "`n3. Testando ativação do ambiente..." -ForegroundColor Yellow
.\start-dev.ps1

Write-Host "`n4. Python atual após ativação:" -ForegroundColor Yellow
python --version

Write-Host "`n=== Configuração Completa ===" -ForegroundColor Cyan
Write-Host "`nPara usar o projeto:" -ForegroundColor White
Write-Host "  1. Execute: .\start-dev.ps1" -ForegroundColor Cyan
Write-Host "  2. Use comandos normalmente: uvicorn, pytest, python" -ForegroundColor Cyan
Write-Host "  3. Para sair: exit" -ForegroundColor Cyan
Write-Host ""
