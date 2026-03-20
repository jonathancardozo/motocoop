from src.domain.corridas.entities import Corrida, StatusCorrida
from src.domain.usuarios.entities import Usuario
from src.domain.shared.value_objects import Endereco
from src.domain.corridas.repositories import ICorridaRepository
from typing import Optional

class SolicitarCorridaUseCase:
    def __init__(self, corrida_repo: ICorridaRepository):
        self.corrida_repo = corrida_repo

    def execute(
        self,
        cliente: Usuario,
        origem: Endereco,
        destino: Endereco,
        valor: Optional[float] = None,
        forma_pagamento: Optional[str] = None
    ) -> Corrida:
        corrida = Corrida(
            id="auto",  # gerar id
            cliente=cliente,
            motorista=None,
            origem=origem,
            destino=destino,
            status=StatusCorrida.SOLICITADA,
            valor=valor,
            forma_pagamento=forma_pagamento,
            solicitacao_ts="auto",  # timestamp atual
        )
        self.corrida_repo.save(corrida)
        return corrida
