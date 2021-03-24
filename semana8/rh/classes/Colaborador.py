from datetime import date


class Colaborador:
    def __init__(self, nome, dia=None, mes=None, ano=None):
        """
        Construtor da classe Colaborador.
        Args:
          nome (string): Nome do colaborador
          dia (int): Dia do aniversario do colaborador
          mes (int): Mes do aniversario do colaborador
          ano (int): Ano do aniversario do colaborador
        Raises:
          ValueError: Erro ocorre quando é informado um tipo errado para a data.
          TypeError: Erro ocorre quando não é informado data.
        """
        self._nome = nome

        if dia is None or mes is None or ano is None:
            raise TypeError('Informe dia, mês e ano')

        if not self._numero_eh_valido(dia):
            raise ValueError("Dia tem que ser um valor numerico inteiro")

        if not self._numero_eh_valido(mes):
            raise ValueError("Mês tem que ser um valor numerico inteiro")

        if not self._numero_eh_valido(ano):
            raise ValueError("Ano tem que ser um valor numerico inteiro")
        
        self._aniversario = date(ano, mes, dia)
               

    def _numero_eh_valido(self, numero):
        return isinstance(numero, int)

    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def aniversario(self):
        return self._aniversario.isoformat()

    def aniversario_hoje(self):
        """
            Método para determinar se a data de aniversario do colaborador é no dia que o método é chamado.
            Return:
               Bool -> True se for aniversario, False se não for.
        """
        hoje = date.today()
        if self._aniversario.day == hoje.day:
            if self._aniversario.month == hoje.month:
                return True
        return False

    def __str__(self):
        return self._nome

    def __repr__(self):
        return 'Colaborador: ' + self._nome
