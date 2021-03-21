from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Classe representa a conta corrente de pessoa juridica.
    Limite padrão da conta: R$ 1500,00
    Args:
        Conta ([type]): [description]
    """
    def __init__(self,  **kwargs):
        """
        Construtor da classe PessoaJuridica.
        Extrai do dicionário kwargs a empresa da pessoa.
        """
        self.empresa = kwargs.get('empresa', '')
        kwargs['limite'] = kwargs.get('limite', 1500)
        super(ContaPessoaJuridica, self).__init__(**kwargs)
