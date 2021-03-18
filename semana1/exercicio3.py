if __name__ == '__main__':
    lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']
    lista_nomes = lista_nomes + ['Mário', 'Arnaldo', 'Lucas', 'Maria Vitória']
    lista_nomes = lista_nomes + ['Vitor', 'Ana Paula', 'Maria Aparecida']
    
    print(*[nome for nome in lista_nomes if len(nome.split(' ')) >= 2], sep='\n')
    