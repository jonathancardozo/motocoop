# Guia de Início Rápido - MotoCoop

## 🚀 Setup Inicial

### 1. Instalar Poetry

```powershell
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 2. Instalar Dependências

```powershell
# Instalar dependências do projeto
poetry install

# Ativar o ambiente virtual
poetry shell
```

### 3. Configurar Variáveis de Ambiente

```powershell
# Copiar exemplo de configuração
cp .env.example .env

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
# Modo desenvolvimento com auto-reload
poetry run uvicorn src.presentation.api.main:app --reload --host 0.0.0.0 --port 8000
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

## 🔧 Comandos Úteis

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
```

## 📝 Próximos Passos

1. ✅ Estrutura básica criada
2. ⏳ Implementar entidades do domínio
3. ⏳ Implementar casos de uso do MVP
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
