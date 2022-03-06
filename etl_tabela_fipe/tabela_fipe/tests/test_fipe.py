import pytest
from tabela_fipe.FipeApi import Fipe
from tabela_fipe.models import TipoDeVeiculo
from tabela_fipe.models import Marca

@pytest.fixture(scope="module")
def fipe():
    return Fipe()

@pytest.fixture(scope="module")
def tipo_veiculo():
    return TipoDeVeiculo(nome='carros')

@pytest.fixture(scope="module")
def marca(tipo_veiculo):
    return Marca(nome='Asia Motors', codigo="5", tipo_de_veiculo=tipo_veiculo)

def test_marcas_is_list(fipe, tipo_veiculo):
    assert isinstance(fipe.marcas(tipo_veiculo), list)

def test_modelos_is_list(fipe, marca):
    assert isinstance(fipe.modelos(marca), list)