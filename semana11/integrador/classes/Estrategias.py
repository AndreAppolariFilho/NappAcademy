from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3
import csv
import re


class Estrategia(ABC):
    """
    Classe Base para as estratégias (algoritmos)

    """
    @abstractmethod
    def execute(self, dados):
        """ Método em que o algoritmo é contido.
        Implementação do algoritmo na classe filha deve
        sobreescrever este método."""
        pass

    @abstractmethod
    def parametros_necessarios(self):
        """Sobreescrever este método para que retorne uma tupla
        com a lista de parâmetros necessários.
        Exemplo:
        ('algoritmo', 'dbname', 'host', 'user', 'password')
        """
        pass

    @abstractmethod
    def nome(self):
        """Sobreescrever este método para que
        retorne o nome do algoritmo utilizado."""
        pass


class Estrategia_SQLite(Estrategia):
    def execute(self, dados):
        lista_registros = []
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas;")
            return [(linha[4], linha[5]) for linha in cursor.fetchall()]

    def parametros_necessarios(self):
        return ('algoritmo', 'db')

    def nome(self):
        return 'Algoritmo SQLite'

class Estrategia_Texto1(Estrategia):
    def execute(self, dados):
        arquivo = open(dados['arquivo'])
        linhas = arquivo.readlines()
        linhas_separadas = [ 
            re.split(r'\s{2,}', linha)
            for linha in linhas[3::]
        ]
        return [(linha[4].strip(), linha[3].strip(), linha[0].strip()) for linha in linhas_separadas] 
    
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')
    
    def nome(self):
        return "Algoritmo Texto Modelo 1"

class Estrategia_Texto2(Estrategia):
    def execute(self, dados):
        arquivo = open(dados['arquivo'])
        linhas = arquivo.readlines()
        linhas_separadas = [ 
            re.split(r'\s{2,}', linha)
            for linha in linhas[3::]
        ]
        return [(linha[1].strip(), linha[2].strip(), linha[0].strip()) for linha in linhas_separadas] 
    
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')
    
    def nome(self):
        return "Algoritmo Texto Modelo 2"

class Estrategia_CSV(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            return [{"total":line['total'], 'vendido_em':line['vendido_em']}for line in reader]

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'
