from datetime import date
from datetime import datetime

class MyCalendar:
    """
    Classe representando o calendario de feriados registrados.
    """
    def __init__(self, *args):
        """
        Contrutor da classe.
        Args:
            args : string de datas no formato dd/mm/YYYY
        """
        self.datas = []
        self._datas_cadastradas = set()
        
        self.add_holiday(*args)
                
    def _convert_date_string(self, date_str):
        """
        Metodo privado utilizado para conversão de string para date
        Return:
            Date: Se foi possivel fazer a conversão retorna a data convertida
            None: Se não foi possivel fazer a conversão retorna None
        """
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError as v:
            return None
            
    def check_holiday(self, date_arg):
        """
        Metodo para saber se uma string de data está registrada como feriado.
        Args:
            date_arg (String) : string de data no formato dd/mm/YYYY
        Return:
            Bool : Representa se a data foi encontrada ou não.
        """
        if isinstance(date_arg, str):
            data_convertida = self._convert_date_string(date_arg)
            return data_convertida in self._datas_cadastradas
        if isinstance(date_arg, date):
            return date_arg in self._datas_cadastradas
        return False

    def add_holiday(self, *args):
        """
        Metodo para adicionar data como feriado.
        Args:
            args : string de datas no formato dd/mm/YYYY
        """
        for date_arg in args:
            if not self.check_holiday(date_arg):
                if isinstance(date_arg, str):
                    data_convertida = self._convert_date_string(date_arg)
                    if data_convertida :
                        self.datas.append(data_convertida)
                        self._datas_cadastradas.add(data_convertida)
                if isinstance(date_arg, date):
                    self.datas.append(date_arg)
                    self._datas_cadastradas.add(date_arg)