"""
Application Settings
Configurações usando Pydantic Settings
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Configurações da aplicação"""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Ambiente
    environment: str = "development"
    
    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True
    
    # PostgreSQL
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "motocoop"
    postgres_user: str = "motocoop_user"
    postgres_password: str = "motocoop_password"
    
    # Database URL
    database_url: Optional[str] = None
    
    @property
    def get_database_url(self) -> str:
        """Constrói a URL do banco de dados"""
        if self.database_url:
            return self.database_url
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
    
    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_password: str = ""
    redis_db: int = 0
    
    @property
    def get_redis_url(self) -> str:
        """Constrói a URL do Redis"""
        if self.redis_password:
            return f"redis://:{self.redis_password}@{self.redis_host}:{self.redis_port}/{self.redis_db}"
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"
    
    # Evolution API (WhatsApp)
    evolution_api_url: str = "http://localhost:8080"
    evolution_api_key: str = "your_evolution_api_key_here"
    evolution_instance_name: str = "motocoop"
    
    # Configurações de Negócio
    valor_km_base: float = 5.00
    tempo_expiracao_corrida_segundos: int = 120
    raio_busca_motorista_km: float = 10.0
    
    # Logging
    log_level: str = "INFO"


# Instância global de settings
settings = Settings()
