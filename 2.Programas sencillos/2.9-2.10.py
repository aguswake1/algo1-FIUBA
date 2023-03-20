# que valor devuelve? devuelve str o none
def domino_generalizado(n: int):
    """Imprime por pantalla todas las fichas de un dominó genérico dado un
    numero arbitrario máximo para las fichas"""

    for i in range(n + 1):
        for j in range(i, n + 1):
            print(i, " | ", j)


# le pasamos como argumento el numero max que queremos que haya en las fichas
domino_generalizado(6)
