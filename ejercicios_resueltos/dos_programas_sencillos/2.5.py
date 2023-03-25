# A.
def es_impar(n: int) -> int:
    """Devuelve 1 si es impar, 0 si es par"""
    return int(n % 2 == 1)  # otra forma: return n%2


# B.
def es_par(n: int) -> int:
    """Devuelve 1 si es par, 0 si es impar"""
    return int(n % 2 == 0)  # otra forma: return 1-n%2


# C.
def cant_caracteres(n: int) -> int:
    """Devuelve cantidad de caracteres de un numero"""
    return len(str(n))


# D.
def multiplo_10_inferior(n: int) -> int:
    """Dado un numero, devuelve el primer multiplo de 10 mas cercano a n"""
    return (n // 10) * 10


print(multiplo_10_inferior(153))  # --> devuelve 150
