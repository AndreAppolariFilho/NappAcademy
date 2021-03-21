from BancoNapp.contas.ContaPessoaFisica import ContaPessoaFisica


class ContaPoupanca(ContaPessoaFisica):
   """
   Classe representa a conta corrente de pessoa juridica.
   Limite padrão da conta: R$ 0,00
   Args:
       Conta ([type]): [description]
   """
   def __init__(self,  **kwargs):
      kwargs['limite'] = kwargs.get('limite', 0)
      super(ContaPoupanca, self).__init__(**kwargs)
   

   def saque(self, valor):
      """
      Método para realizar saque.
      Este método suporta somente números maiores que zero.
      Args:
          valor (float ou int): Valor positivo do saque
      Raises:
          ValueError: Erro ocorre quando é informado valor negativo.
          TypeError: Quando o tipo passado não for inteiro ou float.
      Returns:
          Float: Valor do saque realizado.
      """
      if isinstance(valor, (float, int)):
         if valor > (self.saldo):
            raise ValueError('Valor do saque supera seu saldo.')
      return super(ContaPoupanca, self).saque(valor)

   def rendimento_aniversario(self, valor):
      """
      Método para realizar rendimento de aniversario.
      Este método suporta somente numeros na faixa [0, 1].
      Args:
          valor (float ou int): Valor positivo da porcentagem do rendimento
      Raises:
          ValueError: Ocorre quando é passado uma valor fora da faixa [0, 1].
          
      """
      if valor < 0 or valor > 1:
         raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
      self.saldo += (self.saldo * valor)
