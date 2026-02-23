"""
FastAPI Main Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="MotoCoop API",
    description="Sistema de gestão de mototáxi via WhatsApp",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configurar adequadamente em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "MotoCoop API",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    """Health check detalhado"""
    return {
        "status": "healthy",
        "database": "ok",  # TODO: implementar verificação real
        "redis": "ok",  # TODO: implementar verificação real
        "whatsapp": "ok"  # TODO: implementar verificação real
    }


# TODO: Incluir routers quando implementados
# from src.presentation.api.v1.corridas import routes as corridas_routes
# from src.presentation.api.v1.motoristas import routes as motoristas_routes
# from src.presentation.api.v1.clientes import routes as clientes_routes
# from src.presentation.api.v1.webhooks import routes as webhooks_routes
#
# app.include_router(corridas_routes.router, prefix="/api/v1/corridas", tags=["corridas"])
# app.include_router(motoristas_routes.router, prefix="/api/v1/motoristas", tags=["motoristas"])
# app.include_router(clientes_routes.router, prefix="/api/v1/clientes", tags=["clientes"])
# app.include_router(webhooks_routes.router, prefix="/api/v1/webhooks", tags=["webhooks"])
