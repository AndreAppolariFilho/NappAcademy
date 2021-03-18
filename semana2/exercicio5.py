from massa_dados_situacao_teste import lista_pessoas

def lista_simples(lista_pessoas):
    if(isinstance(lista_pessoas, list)):
        return list(map(lambda x: (x[0], x[-1]), lista_pessoas))
    return []

def teste_1():
    pedaco = slice(0, 2)
    entrada = lista_pessoas[pedaco]
    saida_esperada = [('daniellemosley',('33.93113', '-117.54866')),('rhodesrichard',('39.00622', '-77.4286'))]
    saida = lista_simples(entrada)
    
    assert(saida == saida_esperada)

def teste_2():
    entrada = []
    saida_esperada = []
    saida = lista_simples(entrada)
    assert(saida == saida_esperada)

def teste_3():
    entrada = 'string'
    saida_esperada = []
    saida = lista_simples(entrada)
    assert(saida == saida_esperada)
    

if __name__ == '__main__':
    teste_1()
    teste_2()
    teste_3()