"""
Logging Configuration
"""
import logging
import sys
from typing import Any

from src.config.settings import settings


def setup_logging() -> None:
    """Configura o sistema de logging"""
    
    # Formato do log
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # Configuração básica
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper()),
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Logger específico para a aplicação
    logger = logging.getLogger("motocoop")
    logger.setLevel(getattr(logging, settings.log_level.upper()))
    
    # Reduzir verbosidade de bibliotecas externas
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """
    Retorna um logger configurado
    
    Args:
        name: Nome do logger (geralmente __name__ do módulo)
    
    Returns:
        Logger configurado
    """
    return logging.getLogger(f"motocoop.{name}")
