import pytest
from tabela_fipe.FipeApi import FipeApi


@pytest.fixture(scope="module")
def fipe_api():
    return FipeApi()


def test_chamada_com_endpoint(fipe_api):
    marcas = fipe_api.get(
        "carros/marcas",
    )
    assert isinstance(marcas, list)


def test_chamada_url_completa(fipe_api):
    marcas = fipe_api.get(
        "https://parallelum.com.br/fipe/api/v1/carros/marcas",
    )
    assert isinstance(marcas, list)