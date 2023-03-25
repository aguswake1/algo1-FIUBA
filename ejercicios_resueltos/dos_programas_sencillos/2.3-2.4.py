def fahrenheit_to_celsius(t_fahrenheit: int) -> int:
    "Conversion de temperatura de F° a Celsius"
    return (t_fahrenheit - 32) * 5/9


def conver_table() -> None:
    "Tabla de conversion de 0 a 120 grados celsius de 10 en 10"
    print("Grados F° | Grados celsius")
    for i in range(0, 121, 10):
        print(i, " | ", fahrenheit_to_celsius(i))


conver_table()
