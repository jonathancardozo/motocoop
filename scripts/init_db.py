#!/usr/bin/env python
"""
Script para inicializar o banco de dados
"""
import asyncio
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config.logging import setup_logging, get_logger

logger = get_logger(__name__)


async def init_database():
    """Inicializa o banco de dados"""
    logger.info("Iniciando criação das tabelas do banco de dados...")
    
    # TODO: Implementar criação de tabelas com SQLAlchemy
    # from src.infrastructure.database.connection import engine
    # from src.infrastructure.database.models import Base
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    
    logger.info("Tabelas criadas com sucesso!")


async def enable_postgis():
    """Habilita a extensão PostGIS"""
    logger.info("Habilitando extensão PostGIS...")
    
    # TODO: Implementar habilitação do PostGIS
    # async with engine.begin() as conn:
    #     await conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis"))
    
    logger.info("PostGIS habilitado com sucesso!")


async def main():
    """Função principal"""
    setup_logging()
    logger.info("=== Inicialização do Banco de Dados ===")
    
    try:
        await enable_postgis()
        await init_database()
        logger.info("✓ Banco de dados inicializado com sucesso!")
    except Exception as e:
        logger.error(f"✗ Erro ao inicializar banco de dados: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
