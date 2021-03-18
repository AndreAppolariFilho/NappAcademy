from ecommerce.classes.Produto import Produto
from ecommerce.classes.Pedido import Pedido


class Loja:
    def __init__(self, nome):
        self._nome = nome
        self._estoque = {}
        self._total_estoque = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def estoque(self):
        return self.estoque
    
    @property
    def estoque_total(self):
        return self._total_estoque

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Nome da Loja => ' + self.nome

    def _quantidade_eh_valida(self, quantidade):
        return quantidade >= 0
    
    def _criar_estoque(self, ean, preco, quantidade):
        self._total_estoque += quantidade
        if self._estoque.get(ean):
            self._estoque[ean]['quantidade'] += quantidade
        else:
            self._estoque[ean] = {
                'produto':Produto(ean=ean, preco=preco),
                'quantidade':quantidade
            }

    def add_estoque(self, ean, preco, quantidade):
        if not self._quantidade_eh_valida(quantidade):
            raise TypeError('Não pode ter estoque negativo')
        self._criar_estoque(ean, preco, quantidade) 

    def quantidade_produtos(self, ean):
        if self._estoque.get(ean):
            return self._estoque[ean]['quantidade']
        return 0

    def _existe_produto(self, ean, quantidade):
        return self._estoque.get(ean) and self._estoque.get(ean)['quantidade'] > 0 and self._estoque.get(ean)['quantidade'] >= quantidade

    def comprar(self, ean, quantidade):
        if self._existe_produto(ean, quantidade):
            self._total_estoque -= 1
            self._estoque[ean]['quantidade'] = max(self._estoque[ean]['quantidade'] - quantidade, 0)
            return self._estoque[ean]['produto']
        return None

    def devolver_carrinho(self, pedido):
        if isinstance(pedido, Pedido):
            self._estoque.update(pedido.itens)
            self._total_estoque -= pedido.quantidade_total
            pedido.zerar_pedido()
            return pedido
        return None