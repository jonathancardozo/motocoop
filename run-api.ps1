# MotoCoop - Run API
# Uso: .\run-api.ps1

# Ativar ambiente
& "C:\Users\Jonathan\AppData\Local\pypoetry\Cache\virtualenvs\motocoop-9ldtuIyD-py3.11\Scripts\Activate.ps1"

# Rodar API
uvicorn src.presentation.api.main:app --reload --host 0.0.0.0 --port 8000
