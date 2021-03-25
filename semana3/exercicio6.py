import csv


def find_start_subtring_credit_card(lista, *paramether):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca os clientes com o número de cartão
    de crédito passado como parâmetro. Pode-se passar diversos parâmetros.
    Returna uma lista vazia, caso nenhum parâmetro seja passado.

    Args:
        lista (List): Lista de tuplas

    Returns:
        List: Lista com os nomes de pessoas com cartão de crédito com 
    """
    nova_lista = list(filter(lambda x : x['credit_card'].startswith(paramether), lista))
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
    print(find_start_subtring_credit_card(lista))
    print(find_start_subtring_credit_card(lista, '222', '223'))
    print(find_start_subtring_credit_card(lista, '222', '223', '224'))
    print(find_start_subtring_credit_card(lista, '5'))