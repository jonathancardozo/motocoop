class Endereco:
    def __init__(
        self,
        rua: str,
        numero: str,
        bairro: str,
        cidade: str,
        estado: str,
        cep: str,
        latitude: float,
        longitude: float
    ):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.latitude = latitude
        self.longitude = longitude
