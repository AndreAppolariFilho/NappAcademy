from produtos.classes.Produtos import Produto
from produtos.classes.Produtos import CocaCola
from produtos.classes.Produtos import Pepsi
from produtos.classes.Produtos import GuaranaAntartica
from produtos.classes.Produtos import Dolly
from produtos.classes.Caracteristicas import Tamanho600ml
from produtos.classes.Caracteristicas import Caracteristicas
import pytest


class TestProdutos:
    def test_class_Pepsi(self):
        msg = 'Pepsi tamanho: 600ml.'
        objeto = Pepsi(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Pepsi)
        assert objeto.operation() == msg

    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 600ml.'
        objeto = CocaCola(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg

    def test_class_GuaranaAntartica(self):
        msg = 'GuaranaAntartica tamanho: 600ml.'
        objeto = GuaranaAntartica(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, GuaranaAntartica)
        assert objeto.operation() == msg

    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 600ml.'
        objeto = Dolly(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg

    def test_class_error_subClass(self):
        msg_erro = "O parametro implementation deve ser sub-classe de Caracteristicas"
        with pytest.raises(TypeError) as error:
            Dolly(list())
        assert str(error.value) == msg_erro

    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Produto "
        msg_erro = msg_erro + "with abstract methods operation"
        with pytest.raises(TypeError) as error:
            Produto()
        assert str(error.value) == msg_erro
