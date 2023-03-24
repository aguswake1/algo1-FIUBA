# Lo resuelvo con la premisa de que n1 < n2
def pares_entre(n1: int, n2: int) -> None:
    """Muestra en pantalla todos los numeros pares entre dos numeros"""
    for i in range(n1 + 2 - n1 % 2, n2, 2):
        print(i)


pares_entre(10, 21)
