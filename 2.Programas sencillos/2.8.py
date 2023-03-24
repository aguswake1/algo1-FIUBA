from os import system
# debo importar la funcion calculoFactorial de 1.5.py


def ingresar_valores(cantidad_factoriales: int) -> None:
    for i in range(1, cantidad_factoriales + 1):
        texto_input = "Ingrese factorial numero " + str(i) + ": "
        # factorial_de = input(f"Hey var = {var} Bye : ") also works
        factorial_de = int(input(texto_input))
        system("clear")
        # por que genera espacio con el "!" ?
        print(factorial_de, "! = ", calculoFactorial(factorial_de))


cantidad_valores = int(
    input("Que cantidad de factoriales quiere que calculemos"))

ingresar_valores(cantidad_valores)
