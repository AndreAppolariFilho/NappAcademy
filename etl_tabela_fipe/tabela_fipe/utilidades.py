from pathlib import Path


def alocar_diretorio(caminho):
    Path(caminho).mkdir(parents=True, exist_ok=True)