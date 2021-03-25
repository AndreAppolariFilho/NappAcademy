from exercicio7 import calculo_porcentagem_entre_0_e_100
import pytest

def test_valor_0():
    assert calculo_porcentagem_entre_0_e_100(10,0) == 0

def test_valor_1():
    assert calculo_porcentagem_entre_0_e_100(10,100) == 10

def test_valor_float():
    assert calculo_porcentagem_entre_0_e_100(10,0.5) == 0.05

def test_valor_50():
    assert calculo_porcentagem_entre_0_e_100(10,50) == 5

def test_valor_porcentagem_negativa():
    msg_erro = "Porcentagem precisa estar entre 0 e 100"
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_100(10,-1)
    assert str(error.value) == msg_erro

def test_valor_porcentagem_acima_100():
    msg_erro = "Porcentagem precisa estar entre 0 e 100"
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_100(10,200)
    assert str(error.value) == msg_erro