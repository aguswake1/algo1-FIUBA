def calculoFactorial(numero: int) -> int:
    "Calcula el factorial de un numero !"
    factorial = 1

    for i in range(2, numero + 1):
        factorial *= i

    return factorial
