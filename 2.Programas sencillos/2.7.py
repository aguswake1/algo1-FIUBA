triangulacion = int(input("Ingrese un numero: "))


def numeros_triangulares(numero: int) -> int:
    numero_triangulado = 0
    for i in range(1, numero + 1):
        numero_triangulado += i
        print(i, " - ", numero_triangulado)


def numeros_triangulares_formula(n: int) -> int:
    for i in range(1, n + 1):
        numero_triangulado = (i * (i + 1)) // 2
        print(i, " - ", numero_triangulado)


# ¿Cuál realiza más operaciones?
numeros_triangulares(triangulacion)
numeros_triangulares_formula(triangulacion)
