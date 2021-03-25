import csv


def find_born_in_month_and_gender(lista, paramether='03', gender='F'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca os clientes nascidos no mês 'paramether'
    E pelo gênero gender.

    Args:
        lista (List): Lista de tuplas
        paramether (str, optional): Mês de nascimento com dois caracteres
        janeiro = '01', Fevereiro = '02' . Padrão '03'.
        gender (str, optional): Gênero ( M ou F) com um caracter. Padrão 'F'.

    Returns:
        List: Lista com os nomes de pessoas que nasceram no mês informado
        e com gênero informado.
    """
    nova_lista = list(filter(lambda x : x['birthdate'].split('-')[1] == paramether and x['gender'] == gender, lista))
    return list(map(lambda x: x['name'], nova_lista))


def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o reader e carrega os dados em uma lista retornada.

    Args:
        path (String): Nome do arquivo

    Returns:
        (List): Lista com todos os registros
    """
    
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        return [row for row in reader]
    return []



if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    print(find_born_in_month_and_gender(lista))
    print(find_born_in_month_and_gender(lista, '01'))
    print(find_born_in_month_and_gender(lista, '01', 'M'))