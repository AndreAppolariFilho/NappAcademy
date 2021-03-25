from exercicio6 import calculo_porcentagem_entre_0_e_1
import pytest

def test_valor_0():
    assert calculo_porcentagem_entre_0_e_1(10,0) == 0

def test_valor_1():
    assert calculo_porcentagem_entre_0_e_1(10,1) == 10

def test_valor_float():
    assert calculo_porcentagem_entre_0_e_1(10,0.5) == 5

def test_valor_porcentagem_negativa():
    msg_erro = "Porcentagem precisa estar entre 0 e 1"
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_1(10,-1)
    assert str(error.value) == msg_erro

def test_valor_porcentagem_acima_1():
    msg_erro = "Porcentagem precisa estar entre 0 e 1"
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_1(10,2)
    assert str(error.value) == msg_erro