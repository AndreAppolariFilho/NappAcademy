def extrair_novos_registros(registros_antigos, registros_novos):
    return list(filter(lambda x : x not in registros_antigos, registros_novos))
    
def teste_1():
    lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
    lista_nova = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]    
    resultado_esperado = [('Pessoa 4', 23), ('Pessoa 5', 24)]
    assert(
        extrair_novos_registros(lista_antiga, lista_nova) == resultado_esperado
    )

def teste_2():
    lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
    lista_nova = [('Pessoa1', 22), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]    
    resultado_esperado = [('Pessoa1', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]
    assert(
        extrair_novos_registros(lista_antiga, lista_nova) == resultado_esperado
    )

if __name__ == '__main__':
    lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
    lista_nova = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]
    print(extrair_novos_registros(lista_antiga, lista_nova))
    teste_1()
    teste_2()