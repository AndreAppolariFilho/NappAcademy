from tabela_fipe.PersistenciaDeDados import salvar_marcas_csv
from tabela_fipe.PersistenciaDeDados import salvar_modelos_csv
from tabela_fipe.Logger import LoggerContexto
from tabela_fipe.FipeApi import Fipe
from tabela_fipe.models import lista_tipos_de_veiculos


if __name__ == '__main__':
    logger = LoggerContexto()

    logger.debug(
        'Iniciando rotina de coleta de dados da FIPE - API',
        LoggerContexto.TipoDeEscrita.AMBOS
    )


    fipe_api = Fipe()

    veiculos = lista_tipos_de_veiculos()

    marcas = []

    for veiculo in veiculos:
        logger.debug(
            f'Consultando marcas referente ao tipo de veiculo {veiculo.nome}',
            LoggerContexto.TipoDeEscrita.AMBOS
        )
        marcas.extend(fipe_api.marcas(veiculo))
        logger.debug(
            f'Exportando marcas referente ao tipo de veiculo {veiculo.nome}',
            LoggerContexto.TipoDeEscrita.AMBOS
        )
        salvar_marcas_csv(marcas)


    for marca in marcas:
        veiculo = marca.tipo_de_veiculo
        logger.debug(
            f'Consultando modelos referente ao tipo de veiculo = {veiculo.nome} e marca {marca.nome}',
            LoggerContexto.TipoDeEscrita.AMBOS
        )
        modelos = fipe_api.modelos(marca)
        logger.debug(
            f'Exportando modelos referente ao tipo de veiculo = {veiculo.nome} e marca {marca.nome}',
            LoggerContexto.TipoDeEscrita.AMBOS
        )
        salvar_modelos_csv( marca, modelos)
    logger.debug(
        'Rotina de extração de dados finalizada',
        LoggerContexto.TipoDeEscrita.AMBOS
    )

    