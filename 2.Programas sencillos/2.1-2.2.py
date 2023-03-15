pesos_iniciales = int(input("Ingrese el dinero inicial: "))
tasa_int = int(input("Ingrese el porcentaje de interes: "))
anios_int = int(input("Ingrese la cantidad de anios para el interes: "))


def formula_interes_compuesto(valor_i: int, interes: int, anios: int) -> int:
    "Calcula tasa de interes para el n-esimo año"
    valor_f = valor_i * (1 + interes/100)**anios
    return valor_f


print("El Capital final es ", round(
    formula_interes_compuesto(pesos_iniciales, tasa_int, anios_int)))
