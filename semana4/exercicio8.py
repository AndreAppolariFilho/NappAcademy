def juros_compostos(valor_inicial, juros, tempo):
    """
    Calculadora de juros compostos
    Args:
        valor_inicial (float): Valor inicial.
        juros (float): Porcentagem dos juros, entre 0% e 100%.
        tempo (int): Tempo em meses.
    """
    if juros < 0 or juros > 100:
        raise ValueError("Juros precisa estar entre 0 e 100")
    if tempo < 0:
        raise ValueError("Tempo tem que ser um numero positivo")
    juros = juros/100
    valor_final = valor_inicial * (1+juros)**tempo
    print(valor_final)
    return round(valor_final, 2)
