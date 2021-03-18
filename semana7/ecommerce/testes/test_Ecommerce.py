from ecommerce.classes.Ecommerce import Loja
from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Pedido import Pedido
import pytest

class TestEcommerce:
    def test_class_declared(self):
        loja = Loja('Lojão Tabajara')
        assert isinstance(loja, Loja)

    def test_instanciar(self):
        loja = Loja('Lojão Tabajara')
        assert loja.nome, 'Lojão Tabajara'

    def test_setters(self):
        loja = Loja('Lojão Tabajara')
        assert loja.nome == 'Lojão Tabajara'
        loja.nome = 'Lojão Tabajara Centro'
        assert loja.nome == 'Lojão Tabajara Centro'
        assert loja.estoque_total == 0

    def test_str_repr(self):
        loja = Loja('Lojão Tabajara')
        assert str(loja) == 'Lojão Tabajara'
        assert repr(loja) == 'Nome da Loja => Lojão Tabajara'

    def test_metodo_add_estoque_ok(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('12345678911', 15, 1)
        assert loja.estoque_total == 1

    def test_metodo_add_estoque_ok2(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('12345678911', 15, 3)
        loja.add_estoque('123', 12, 5)
        assert loja.estoque_total == 8

    def test_metodo_add_estoque_negativo(self):
        loja = Loja('Lojão Tabajara')
        msg_erro = 'Não pode ter estoque negativo'
        with pytest.raises(TypeError) as error:
            loja.add_estoque('12345', 20, -1)
        assert str(error.value) == msg_erro
        
    def test_quantidade_produtos(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 10)
        loja.add_estoque('1234', 20, 5)
        msg_erro = 'Não pode ter estoque negativo'
        with pytest.raises(TypeError) as error:
            loja.add_estoque('12345', 20, -1)
        assert str(error.value) == msg_erro
        loja.add_estoque('123456', 20, 0)
        assert loja.quantidade_produtos('123') == 10
        assert loja.quantidade_produtos('1234') == 5
        assert loja.quantidade_produtos('12345') == 0
        assert loja.quantidade_produtos('123456') == 0

    def test_metodo_comprar_ok(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 3)
        assert loja.estoque_total == 3
        loja.comprar('123', 1)
        assert loja.estoque_total == 2

    def test_metodo_comprar_sem_produto(self):
        loja = Loja('Lojão Tabajara')
        assert loja.comprar('9999999', 1) is None

    def test_metodo_comprar_com_valor_negativo(self):
        loja = Loja('Lojão Tabajara')
        assert loja.comprar('9999999', -1) is None
    
    def test_metodo_comprar_mais_que_estoque(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('9999999', 15, 1)
        assert loja.comprar('9999999', 2) is None

    def test_metodo_comprar_ok2(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 1)
        assert loja.estoque_total == 1
        loja.comprar('123', 1)
        assert loja.estoque_total == 0
        assert loja.comprar('123', 1) is None

    def test_devolver_carrinho(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 10)
        loja.add_estoque('1234', 20, 5)
        assert loja.estoque_total == 15
        cliente = Cliente('John Doe')
        pedido = Pedido(cliente)
        pedido.add_item(loja.comprar('1234', 1), 1)
        pedido.add_item(loja.comprar('123', 1), 1)
        assert pedido.quantidade_total == 2
        assert loja.estoque_total == 13
        assert loja.quantidade_produtos('1234') == 4
        assert loja.quantidade_produtos('123') == 9
        loja.devolver_carrinho(pedido)
        assert pedido.quantidade_total == 0
        assert loja.estoque_total == 11