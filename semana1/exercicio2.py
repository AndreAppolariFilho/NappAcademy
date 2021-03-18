import re
if __name__ == '__main__':
    lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'elen']
    vogais = ['A', 'E', 'I', 'O', 'U']
    for nome in lista_nomes:
        if re.match("^[aeiouAEIOU].*",nome):
            print(nome)
