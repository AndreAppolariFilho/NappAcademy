from exercicio8 import juros_compostos

import pytest

def test_valor_0():
    assert juros_compostos(10,0, 1) == 10

def test_valor_juros_100():
    assert juros_compostos(10,100, 1) == 20

def test_valor_juros_50():
    assert juros_compostos(10,50, 1) == 15

def test_valor_juros_negativo():
    msg_erro = "Juros precisa estar entre 0 e 100"
    with pytest.raises(ValueError) as error:
        juros_compostos(10,-1, 1)
    assert str(error.value) == msg_erro

def test_valor_juros_maior_que_100():
    msg_erro = "Juros precisa estar entre 0 e 100"
    with pytest.raises(ValueError) as error:
        juros_compostos(10,200, 1)
    assert str(error.value) == msg_erro


def test_valor_juros_mes_negativo():
    msg_erro = "Tempo tem que ser um numero positivo"
    with pytest.raises(ValueError) as error:
        juros_compostos(10,100, -1)
    assert str(error.value) == msg_erro
    
