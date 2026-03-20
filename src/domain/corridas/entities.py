from enum import Enum
from typing import Optional
from src.domain.usuarios.entities import Usuario
from src.domain.shared.value_objects import Endereco

class StatusCorrida(Enum):
    SOLICITADA = "solicitada"
    DESPACHADA = "despachada"
    ACEITA = "aceita"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDA = "concluida"
    CANCELADA_CLIENTE = "cancelada_cliente"
    CANCELADA_MOTORISTA = "cancelada_motorista"
    EXPIRADA = "expirada"

class Corrida:
    def __init__(
        self,
        id: str,
        cliente: Usuario,
        motorista: Optional[Usuario],
        origem: Endereco,
        destino: Endereco,
        status: StatusCorrida,
        valor: Optional[float] = None,
        forma_pagamento: Optional[str] = None,
        solicitacao_ts: Optional[str] = None,
        inicio_ts: Optional[str] = None,
        conclusao_ts: Optional[str] = None,
        motivo_cancelamento: Optional[str] = None,
        distancia: Optional[float] = None
    ):
        self.id = id
        self.cliente = cliente
        self.motorista = motorista
        self.origem = origem
        self.destino = destino
        self.status = status
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.solicitacao_ts = solicitacao_ts
        self.inicio_ts = inicio_ts
        self.conclusao_ts = conclusao_ts
        self.motivo_cancelamento = motivo_cancelamento
        self.distancia = distancia
