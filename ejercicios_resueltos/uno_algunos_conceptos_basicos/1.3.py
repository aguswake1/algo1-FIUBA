from Math import PI, sqrt


def perimetroRectangulo(b: int, h: int) -> int:
    "Calcula el perímetro de un rectángulo"
    return 2 * (b + h)


def areaRectangulo(b: int, h: int) -> int:
    "Calcula el área de un rectángulo"
    return b * h


def areaRectangulo(x1: int, x2: int, y1: int, y2: int) -> int:
    "Calcula el área de un rectángulo dado 4 coordenadas"
    return (x2 - x1) * (y2 - y1)


def perimetroCirculo(radio: int) -> int:
    "Calcula el perímetro de un círculo"
    return 2 * PI * radio


def areaCirculo(radio: int) -> int:
    "Calcula el area de un círculo"
    return PI * radio**2


def volumenEsfera(radio: int) -> int:
    "Calcular el volumen de una esfera"
    return 4/3 * PI * radio**3


def teoremaPitagoras(c1: int, c2: int) -> int:
    "Usa el teorema de Pitagoras"
    hipotenusa = sqrt(c1**2 + c2**2)
    return hipotenusa
