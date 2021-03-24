from rh.classes.Colaborador import Colaborador


class Departamento:
    """
    Classe representa o departamento.
    """
    def __init__(
        self, 
        nome_setor, 
        nome_responsavel,
        dia_aniversario, 
        mes_aniversario, 
        ano_aniversario
    ):
        """
        Construtor da classe Departamento.
        Args:
          nome_setor (string): Nome do setor
          nome_responsavel (string): Nome do responsavel
          dia_aniversario (int): Dia do aniversario do responsavel
          mes_aniversario (int): Mes do aniversario do responsavel
          ano_aniversario (int): Ano do aniversario do responsavel
        Raises:
          ValueError: Erro ocorre quando é informado um tipo errado para a data.
        """
        self._nome_setor = nome_setor
        self._colaboradores = []
        self.informar_responsavel(nome_responsavel, dia_aniversario, mes_aniversario, ano_aniversario)

    @property
    def nome(self):
        return self._nome_setor

    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        return str(self._responsavel)

    @property
    def colaboradores(self):
        return self._colaboradores

    def informar_responsavel(self, nome, dia, mes, ano):
        """
            Método para atualizar responsavel.
            Args:
                nome (string): Nome do responsavel
                dia (int): Dia do aniversario do responsavel
                mes (int): Mes do aniversario do responsavel
                ano (int): Ano do aniversario do responsavel
            Raises:
                ValueError: Erro ocorre quando é informado um tipo errado para a data.
        """
        self._responsavel = Colaborador(nome, dia, mes, ano)

    def add_colaborador(self, nome, dia, mes, ano):
        """
            Método para adicionar colaborador.
            Args:
                nome (string): Nome do colaborador
                dia (int): Dia do aniversario do colaborador
                mes (int): Mes do aniversario do colaborador
                ano (int): Ano do aniversario do colaborador
            Raises:
                ValueError: Erro ocorre quando é informado um tipo errado para a data.
        """
        self._colaboradores.append(Colaborador(nome, dia, mes, ano))

    def verificar_aniversariantes(self):
        """
            Método para retornar lista de aniversariantes.
            Return:
                List -> Contendo o nome do colaborador, a data de aniversario e o setor que ele participa
        """
        lista = [ 
            (colaborador.nome, colaborador.aniversario, self._nome_setor) 
            for colaborador in self.colaboradores 
            if colaborador.aniversario_hoje()
        ]
        if self._responsavel.aniversario_hoje():
            lista.append((self._responsavel.nome, self._responsavel.aniversario, self._nome_setor))
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor
