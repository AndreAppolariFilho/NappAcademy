from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Produto import Produto


class Pedido:
    formas_aceitas = ['dinheiro', 'cartão', 'pix']

    def __init__(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente
            self._itens = {}
            self._preco_total = 0
            self._quantidade_total = 0
            return
        raise TypeError('Não é possível instanciar um Pedido sem um cliente')

    @property
    def itens(self):
        return self._itens

    @property
    def quantidade_total(self):
        return self._quantidade_total

    @property
    def cliente(self):
        return self._cliente

    def zerar_pedido(self):
        self._itens = {}
        self._quantidade_total = 0

    def __str__(self):
        return 'Pedido de ' + str(self._cliente)

    def __repr__(self):
        return 'Pedido de ' + str(self._cliente)

    def _quantidade_eh_valida(self, quantidade):
        return quantidade >= 0
    
    def _criar_iten(self, produto, quantidade):
        self._preco_total += quantidade * produto.preco
        self._quantidade_total += quantidade
        if self._itens.get(produto.ean):
            
            self._itens[produto.ean]['quantidade'] += quantidade
        else:
            self._itens[produto.ean] = {
                'quantidade':quantidade,
                'produto':produto
            }

    def add_item(self, produto, quantidade):
        if not self._quantidade_eh_valida(quantidade):
            raise TypeError('Quantidadr negativa não é permitido')    
        if not isinstance(produto, Produto):
            raise TypeError('Não foi passado um objeto produto')
        self._criar_iten(produto, quantidade)

    def quantidade_produto_no_pedido(self, ean):
        if self._itens.get(ean):
            return self._itens[ean]['quantidade']
        return 0

    def nota_fiscal(self):
        return list(map(lambda x: (x[0], str(x[1]['quantidade'])), self._itens.items()))

    def valor_total_pagar(self):
        return self._preco_total
    
    def _forma_pagamento_eh_aceita(self, forma_pagamento):
        return forma_pagamento.lower() in self.__class__.formas_aceitas

    def checkout(self, forma_pagamento=None):
        if forma_pagamento is None:
            raise Exception('Informe um meio de pagamento')
        if self._forma_pagamento_eh_aceita(forma_pagamento.lower()):
            dados_checkout = (self.nota_fiscal(), self.valor_total_pagar())
            return dados_checkout
        raise Exception('Forma de pagamento não aceita')