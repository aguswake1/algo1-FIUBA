"""
# Operadores: corto circuito
def f():
    print("en f")
    return False


def g():
    print("en g")
    return True


r = f() and g()
# no imprime g() porque detecta que es un and y f() es falsa
print(r)

# --------------------------------------------------------------------
cuando checkeamos una condicion con un int o un str, el interprete
automaticamente y de manera implicita hace un bool(condicion)
# --------------------------------------------------------------------


# early return
def transferir(cuenta_origen, cuenta_destino, cant, msg):
    if not existe(cuenta_origen):
        return ERROR_CUENTA_ORIGEN
    if not existe(cuenta_destino):
        return ERROR_CUENTA_DESTINO
    if cant > saldo(cuenta_origen):
        return ERROR_SALDO
    Por leyes de De Morgan: ¬(A ∩ B) = ¬A ∪ ¬B
Sea x ∈ ¬(A∩B) ⇒ x ∉ A ∩ B ⇒ x ∉ A o x ∉ B ⇒x ∈ ¬A ∪ ¬B
    # if not (s is not None and s != ""):
    # if not (s is not None) or not (s != ""):
    if (s is None) or (s == ""):
        return ERROR_MSG_VACIO

    _transferir(cuenta_origen, cuenta_destino, cant, msg)
    return EXITO


for es ciclo definido.
∀ x ∈ <iterable>:
    procesar x

while es un ciclo indefinido
mientras <condicion>
    hacer cosas

Patron ciclo con centinela
repetir indefinidamente:
    leer valor
    si valor = centinela:
        cortar el ciclo (break)
    procesar valor
"""


# Default parameters && type hinting
def mostrar_coords(columnas: int = 5, filas: int = 3) -> None:
    for rows in range(filas):
        for col in range(columnas):
            print(1, end=" ")
        print("")


mostrar_coords()
