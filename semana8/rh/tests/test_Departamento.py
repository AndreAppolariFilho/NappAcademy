from rh.classes.Departamento import Departamento
from datetime import date, timedelta
import pytest

class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ', 'José da Silva', 1, 1, 1990)
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ', 'José da Silva', 1, 1, 1990)
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel == 'José da Silva'

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria','José da Silva', 1, 1, 1990)
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'
    
    def test_responsavel_erro_dia_invalido(self):
        msg_erro = "Dia tem que ser um valor numerico inteiro"
        with pytest.raises(ValueError) as error:
            departamento = Departamento('Departamento XYZ','José da Silva', 1.5, 1, 1990)
        assert str(error.value) == msg_erro
    
    def test_responsavel_erro_mes_invalido(self):
        msg_erro = "Mês tem que ser um valor numerico inteiro"
        with pytest.raises(ValueError) as error:
            departamento = Departamento('Departamento XYZ','José da Silva', 1, 1.5, 1990)
        assert str(error.value) == msg_erro
    
    def test_responsavel_erro_ano_invalido(self):
        msg_erro = "Ano tem que ser um valor numerico inteiro"
        with pytest.raises(ValueError) as error:
            departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, '1990')
        assert str(error.value) == msg_erro

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'
        departamento.informar_responsavel('João Oliveira', 1, 1, 1990)
        assert departamento.responsavel == 'João Oliveira'

    def test_responsavel_substituido_erro_dia_invalido(self):
        msg_erro = "Dia tem que ser um valor numerico inteiro"
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        with pytest.raises(ValueError) as error:
            departamento.informar_responsavel('João Oliveira', '1', 1, 1990)
        assert str(error.value) == msg_erro
    
    def test_responsavel_substituido_erro_mes_invalido(self):
        msg_erro = "Mês tem que ser um valor numerico inteiro"
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)        
        with pytest.raises(ValueError) as error:
            departamento.informar_responsavel('João Oliveira', 1, '1', 1990)
        assert str(error.value) == msg_erro
    
    def test_responsavel_substituido_erro_ano_invalido(self):
        msg_erro = "Ano tem que ser um valor numerico inteiro"
        departamento = Departamento('Departamento XYZ','José da Silva', 1, 1, 1990)
        with pytest.raises(ValueError) as error:
            departamento.informar_responsavel('João Oliveira', 1, 1, '1990')
        assert str(error.value) == msg_erro

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ', 'José da Silva', 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2
    
    def test_add_colaborador_erro_dia_invalido(self):
        msg_erro = "Dia tem que ser um valor numerico inteiro"
        departamento = Departamento('Departamento XYZ', 'José da Silva', 1, 1, 1990)
        with pytest.raises(ValueError) as error:
            departamento.add_colaborador('João Oliveira', '18', 3, 1992)
        assert str(error.value) == msg_erro

    def test_add_colaborador_erro_mes_invalido(self):
        msg_erro = "Mês tem que ser um valor numerico inteiro"
        departamento = Departamento('Departamento XYZ', 'José da Silva', 1, 1, 1990)
        with pytest.raises(ValueError) as error:
            departamento.add_colaborador('João Oliveira', 18, '3', 1992)
        assert str(error.value) == msg_erro

    def test_add_colaborador_erro_ano_invalido(self):
        msg_erro = "Ano tem que ser um valor numerico inteiro"
        departamento = Departamento('Departamento XYZ', 'José da Silva', 1, 1, 1990)
        with pytest.raises(ValueError) as error:
            departamento.add_colaborador('João Oliveira', 18, 3, '1992')
        assert str(error.value) == msg_erro

    def test_verificar_aniversariantes(self):
        hoje = date.today()
        today_str = '{}-{}'.format(str(hoje.month).zfill(2), str(hoje.day).zfill(2))
        retorno = [('João Oliveira', '1992-'+today_str,'Departamento XYZ'),
                   ('Luis Fernando', '2000-'+today_str,'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        depto = Departamento('Departamento XYZ', 'José da Silva', dt1.day, dt1.month, 1990)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list

    def test_verificar_aniversariantes_nome_multiplos_departamentos(self):
        hoje = date.today()
        today_str = '{}-{}'.format(str(hoje.month).zfill(2), str(hoje.day).zfill(2))
        retorno = [('João Oliveira', '1992-'+today_str,'Departamento XYZ'),
                   ('Luis Fernando', '2000-'+today_str,'Departamento 123')]
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        depto = Departamento('Departamento XYZ', 'José da Silva', dt1.day, dt1.month, 1990)
        depto2 = Departamento('Departamento 123', 'Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        
        depto2.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto2.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        aniversariantes.extend(depto2.verificar_aniversariantes())
        assert aniversariantes == retorno
        

    def test_verificar_aniversariantes_responsavel_faz_aniversario(self):
        hoje = date.today()
        today_str = '{}-{}'.format(str(hoje.month).zfill(2), str(hoje.day).zfill(2))
        retorno = [('João Oliveira', '1992-'+today_str,'Departamento XYZ'),
                   ('Luis Fernando', '2000-'+today_str,'Departamento XYZ'),
                   ('José da Silva', '1990-'+today_str,'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=4)
        depto = Departamento('Departamento XYZ', 'José da Silva', hoje.day, hoje.month, 1990)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 3
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list
