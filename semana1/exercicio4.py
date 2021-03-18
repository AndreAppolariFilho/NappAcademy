def gera_novo_nome(nome):
    return ''.join(['| {} '.format(caracter) for caracter in nome]) + '|'

    
if __name__ == '__main__':
    lista_nomes = ['Ana', 'Ana Maria', 'Pedro', 'Elena', 'Helena', 'Elen']

    print(*[gera_novo_nome(nome) for nome in lista_nomes ],sep='\n')