import csv
import json


def carregar_dicionario_websites(path):
    """
    Função que recebe o nome do arquivo .CSV
    e extrai um dicionário, com usernames como chave e tupla de URLs.

    Args:
        path (String): Nome do arquivo

    Returns:
        Dicionário: Dicionário, cuja chave é o username
        e o valor são tuplas com URLs de websites.
    """
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        return [row for row in reader]
    return []



if __name__ == "__main__":
    path = 'names.csv'
    dicionario = {}
    dicionario = carregar_dicionario_websites(path)
    json_object = json.dumps(dicionario, indent=4)
    print(json_object)