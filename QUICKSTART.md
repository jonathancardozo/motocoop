# Guia de Início Rápido - MotoCoop

## 🚀 Setup Inicial

### 0. Pré-requisitos

**Python 3.11+ Recomendado**
- Baixe de: https://www.python.org/downloads/
- ⚠️ **Importante**: Durante instalação, marque "Add Python to PATH"
- Evite Python da Microsoft Store (causa problemas com Poetry)

**Verificar versões disponíveis:**
```powershell
py --list
# Deve mostrar Python 3.11 ou superior
```

### 1. Instalar Poetry

```powershell
# Instalar Poetry usando Python 3.11
py -3.11 -m pip install --user poetry

# Verificar instalação
py -3.11 -m poetry --version
```

**Adicionar Poetry ao PATH (Opcional, mas recomendado):**
```powershell
# Executar PowerShell como Administrador
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:APPDATA\Python\Python311\Scripts", "User")

# Fechar e reabrir PowerShell, depois testar:
poetry --version
```

### 2. Configurar Projeto com Python 3.11

```powershell
# Navegar até o diretório do projeto
cd C:\projetos-pessoais-software\motocoop

# Configurar Poetry para usar Python 3.11
poetry env use 3.11

# Instalar dependências do projeto
poetry install
```

**Se Poetry não estiver no PATH, use:**
```powershell
& "$env:APPDATA\Python\Python311\Scripts\poetry.exe" env use 3.11
& "$env:APPDATA\Python\Python311\Scripts\poetry.exe" install
```

### 3. Configurar Variáveis de Ambiente

```powershell
# Copiar exemplo de configuração
copy .env.example .env

# Editar .env com suas configurações
notepad .env
```

### 4. Iniciar Serviços com Docker

```powershell
# Subir PostgreSQL, Redis e Evolution API
docker-compose up -d postgres redis evolution-api

# Verificar se os serviços estão rodando
docker-compose ps
```

### 5. Inicializar Banco de Dados

```powershell
# Executar script de inicialização (quando implementado)
poetry run python scripts/init_db.py
```

### 6. Executar a API

```powershell
# Se Poetry está no PATH:
poetry run uvicorn src.presentation.api.main:app --reload --host 0.0.0.0 --port 8000

# Se Poetry NÃO está no PATH (Windows):
& "$env:APPDATA\Python\Python311\Scripts\poetry.exe" run uvicorn src.presentation.api.main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🧪 Executar Testes

```powershell
# Todos os testes
poetry run pytest

# Com cobertura
poetry run pytest --cov=src

# Apenas testes unitários
poetry run pytest tests/unit

# Apenas testes de integração
poetry run pytest tests/integration
```

## 🔍 Qualidade de Código

```powershell
# Formatar código com Black
poetry run black src tests

# Lint com Ruff
poetry run ruff check src tests

# Type checking com Mypy
poetry run mypy src
```

## 🐳 Docker Compose Completo

```powershell
# Subir toda a stack (incluindo a API)
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar todos os serviços
docker-compose down

# Parar e remover volumes (⚠️ apaga dados)
docker-compose down -v
```

## 📊 Acessar Serviços

- **API FastAPI**: http://localhost:8000
- **Evolution API**: http://localhost:8080
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379
**Se Poetry está no PATH:**
```powershell
# Adicionar nova dependência
poetry add nome-do-pacote

# Adicionar dependência de desenvolvimento
poetry add --group dev nome-do-pacote

# Atualizar dependências
poetry update

# Ver dependências instaladas
poetry show

# Executar script Python
poetry run python seu_script.py

# Entrar no shell do ambiente virtual
poetry shell
```

**Se Poetry NÃO está no PATH (Windows):**
```poPython 3.11+ instalado
2. ✅ Poetry configurado
3. ✅ Estrutura básica criada
4. ✅ API funcionando
5. ⏳ Implementar entidades do domínio
6. ⏳ Implementar casos de uso do MVP
7. ⏳ Configurar banco de dados e models
8. ⏳ Integrar Evolution API
9. ⏳ Implementar endpoints REST
10. ⏳ Testes automatizados

## ⚠️ Importante

- Nunca commitar o arquivo `.env` (já está no .gitignore)
- Alterar as senhas padrão antes de ir para produção
- Configurar CORS adequadamente para produção
- Revisar configurações de segurança do Evolution API

## 🔧 Troubleshooting

### Poetry não encontrado após instalação
```powershell
# Adicionar ao PATH permanentemente
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:APPDATA\Python\Python311\Scripts", "User")
# Fechar e reabrir PowerShell
```

### Erro ao criar virtualenv no Windows
Se você instalou Python da Microsoft Store, desinstale e instale do python.org

### Múltiplas versões do Python
```powershell
# Listar versões disponíveis
py --list

# Usar versão específica
py -3.11 -m poetry install
```
4. ⏳ Configurar banco de dados e models
5. ⏳ Integrar Evolution API
6. ⏳ Implementar endpoints REST
7. ⏳ Testes automatizados
8. ⏳ Documentação de APIs

## ⚠️ Importante

- Nunca commitar o arquivo `.env` (já está no .gitignore)
- Alterar as senhas padrão antes de ir para produção
- Configurar CORS adequadamente para produção
- Revisar configurações de segurança do Evolution API
