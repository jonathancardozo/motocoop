from src.application.centrais.cadastrar_central import CadastrarCentralUseCase

class FakeCentralRepo:
    def __init__(self):
        self.saved = []
    def save(self, central):
        self.saved.append(central)

def test_cadastrar_central():
    repo = FakeCentralRepo()
    usecase = CadastrarCentralUseCase(repo)
    central = usecase.execute(
        id="central1",
        nome="Central Teste",
        area_cobertura={"poligono": [[-10.0, -20.0], [-11.0, -21.0]]},
        administradores=["12345678900"]
    )
    assert central.id == "central1"
    assert central.nome == "Central Teste"
    assert repo.saved[0] == central
