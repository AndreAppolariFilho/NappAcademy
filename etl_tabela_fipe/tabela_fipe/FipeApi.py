from .models import Marca
from .models import Modelo
from .models import TipoDeVeiculo
from urllib.parse import urljoin
import shlex
import json
import subprocess


class FipeApi:
    URL = 'https://parallelum.com.br/fipe/api/v1/'

    def get(self, url):
        if not url.startswith("http"):
            url = urljoin(self.URL, url)
        cmd = f"curl --location --request GET '{url}'"
        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = process.communicate()
        return json.loads(stdout.decode('utf-8'))


class Fipe:
    def __init__(self):
        self.fipe_api = FipeApi()

    def marcas(self, veiculo: TipoDeVeiculo)->list[Marca]:
        marcas = self.fipe_api.get(
            f"{veiculo.nome}/marcas",
        )
        return [
            Marca(
                **marca,
                tipo_de_veiculo=veiculo
            ) 
            for marca in marcas
        ]
    
    def modelos(self,  marca: Marca)->list[Modelo]:
        modelos = self.fipe_api.get(
            f"{marca.tipo_de_veiculo.nome}/marcas/{marca.codigo}/modelos"
        )['modelos']

        return [
            Modelo(
               **modelo,
                marca=marca
            ) 
            for modelo in modelos
        ]

    
        