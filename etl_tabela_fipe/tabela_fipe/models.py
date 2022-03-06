from pydantic import BaseModel


class TipoDeVeiculo(BaseModel):
    nome: str


class Marca(BaseModel):
    nome:str
    codigo:str
    tipo_de_veiculo: TipoDeVeiculo

    class Config:
        json_encoders = {
            'TipoDeVeiculo': lambda a: a.nome
        }


class Modelo(BaseModel):
    nome:str
    codigo:int
    marca: Marca

    class Config:
        json_encoders = {
            Marca: lambda a: a.codigo
        }

def lista_tipos_de_veiculos()-> list[TipoDeVeiculo]:
    return [TipoDeVeiculo(nome=tipo) for tipo in ['carros', 'motos', 'caminhoes']]
