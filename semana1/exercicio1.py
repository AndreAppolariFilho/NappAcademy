if __name__ == '__main__':
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    print('Seu nome é: {nome}'.format(nome=nome))
    print('Sua idade daqui a cinco anos será: {idade}'.format(
            idade=(idade+5)
        )
    )