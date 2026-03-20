from typing import List

class Central:
    def __init__(
        self,
        id: str,
        nome: str,
        area_cobertura: object,  # polígono
        administradores: List[str]  # lista de CPFs
    ):
        self.id = id
        self.nome = nome
        self.area_cobertura = area_cobertura
        self.administradores = administradores
