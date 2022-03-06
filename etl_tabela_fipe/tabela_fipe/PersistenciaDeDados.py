from abc import ABC, abstractmethod
import pandas as pd
from decouple import config
from tabela_fipe.utilidades import alocar_diretorio
import json
from tabela_fipe.models import Marca
from tabela_fipe.models import Modelo
from tabela_fipe.models import TipoDeVeiculo


class PersistenciaDeDados(ABC):
    
    @abstractmethod
    def salvar_dados(self, dados):
        pass


class PersistenciaDeDadosCSV(PersistenciaDeDados):

    def __init__(self, local_do_arquivo):
        self.local_do_arquivo = local_do_arquivo

    def salvar_dados(self, dados):
        df = pd.DataFrame(dados)
        df.to_csv(
            self.local_do_arquivo, 
            sep=';', 
            encoding='utf-8', 
            index=False
        )


def salvar_modelos_csv(marca: Marca, modelos: list[Modelo]):
    alocar_diretorio(f'{config("caminho_arquivos")}\\Modelos')
    alocar_diretorio(f'{config("caminho_arquivos")}\\Modelos\\\{marca.tipo_de_veiculo.nome}')
    persistencia_de_dados = PersistenciaDeDadosCSV(
        f'{config("caminho_arquivos")}\\Modelos\\\{marca.tipo_de_veiculo.nome}\\Modelos_{marca.nome}.csv'
    )
    persistencia_de_dados.salvar_dados([json.loads(modelo.json(models_as_dict=False)) for modelo in modelos])


def salvar_marcas_csv(marcas: list[Marca]):
    alocar_diretorio(f'{config("caminho_arquivos")}\\Marcas')
    persistencia_de_dados = PersistenciaDeDadosCSV(
        f'{config("caminho_arquivos")}\\Marcas\\TabelaDeMarcas.csv')
    persistencia_de_dados.salvar_dados([json.loads(marca.json(models_as_dict=False)) for marca in marcas])

