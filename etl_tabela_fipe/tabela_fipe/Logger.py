import logging
from enum import IntEnum
import sys
from logging.handlers import RotatingFileHandler
from decouple import config
from tabela_fipe.utilidades import alocar_diretorio


class CustomRotatingFileHandler(RotatingFileHandler):

    def __init__(self, filename: str, num_files=5, *args, **kwargs):
        self.maxBytes = 5 * 1024 * 1024
        self.backupCount = num_files
        super(RotatingFileHandler, self).__init__(
            filename, 
            mode='a',
            *args,
            **kwargs
        )


class Logger:
    def __init__(self, handler, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s |  %(levelname)s: %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.handlers = []
        self.logger.addHandler(handler)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def critical(self, msg):
        self.logger.critical(msg)


class LoggerContexto:
    class TipoDeEscrita(IntEnum):
        ARQUIVO = 0
        STDOUT = 1
        AMBOS = 2

    def __init__(self):
        alocar_diretorio(f'{config("caminho_arquivos")}\\LOG')

    def __cria_logger_file(self):
        return Logger(
                CustomRotatingFileHandler(f'{config("caminho_arquivos")}\\LOG\\log_execucao.log'),
                'file'
            )

    def __cria_logger_stdout(self):
        return Logger(
                logging.StreamHandler(sys.stdout),
                'std'
            )

    def debug(self, mensagem:str, tipo_de_escrita: TipoDeEscrita):
        if tipo_de_escrita == LoggerContexto.TipoDeEscrita.AMBOS:
            self.__cria_logger_file().debug(mensagem)
            self.__cria_logger_stdout().debug(mensagem)
        elif tipo_de_escrita == LoggerContexto.TipoDeEscrita.ARQUIVO:
            self.__cria_logger_file().debug(mensagem)
        elif tipo_de_escrita == LoggerContexto.TipoDeEscrita.STDOUT:
            self.__cria_logger_stdout().debug(mensagem)

