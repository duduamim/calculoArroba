def calculo_valor_arroba(peso_vivo, preco_arroba):
    """
    Calcula o peso em arrobas e o valor total baseado no peso vivo e no preço por arroba.
    """
    peso_vivo_half = peso_vivo / 2  # Metade do peso vivo
    peso_arroba = peso_vivo_half / 15  # Peso em arrobas
    valor_total = peso_arroba * preco_arroba  # Calcula o valor total
    return peso_arroba, valor_total
