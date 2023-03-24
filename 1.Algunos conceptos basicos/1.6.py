def operacionesBasicas(n1: int, n2: int) -> None:
    "suma, resta, multiplica y divide dos numeros"
    print(n1 + n2, n1 - n2, n1 / n2, n1 * n2)


def tablaMultiplicar(num: int) -> None:
    "Tabla de multiplicar de un numero n"
    for i in range(1, 11):
        print("{} x {} = {} ".format(num, i, num * i))
