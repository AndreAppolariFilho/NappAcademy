import csv

def find_subtring_credit_card(lista, parametro='322'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca a string 'parâmetro' como substring
    do campo 'Cartão de Crédito'.

    Args:
        lista (List): [description]
        parametro (str, optional): Substring a ser encontrada. Padrão '322'.

    Returns:
        List: Lista com os nomes de pessoas que possuam substring
        no cartão de crédito
    """
    nova_lista = list(filter(lambda x : parametro in x['credit_card'], lista))
    return list(map(lambda x: x['name'], nova_lista))

def find_start_subtring_credit_card(lista, parametro='303'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca a string 'parâmetro' como início
    do campo 'Cartão de Crédito'.

    Args:
        lista (List): [description]
        parametro (str, optional): Substring a ser encontrada. Padrão '303'.

    Returns:
        List: Lista com os nomes de pessoas que possuam substring
        no cartão de crédito
    """
    nova_lista = list(filter(lambda x : x['credit_card'].startswith(parametro), lista))
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
    print(find_subtring_credit_card(lista))
    print(find_subtring_credit_card(lista, '222'))
    print(find_start_subtring_credit_card(lista, '222'))