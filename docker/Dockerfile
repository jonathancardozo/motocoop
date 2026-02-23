FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY pyproject.toml ./

# Configurar Poetry para não criar virtualenv
RUN poetry config virtualenvs.create false

# Instalar dependências
RUN poetry install --no-interaction --no-ansi

# Copiar código da aplicação
COPY . .

# Expor porta
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "src.presentation.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
