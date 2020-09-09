from math import pi, pow, sqrt, atan

# Funciones
def hipotenusa(x, y):
    """
    calculo de la hipotenusa de un triangulo rectangulo
    :param x: cateto horizontal
    :param y: cateto vertical
    :return: hipotenusa
    """
    return sqrt(pow(x, 2) + pow(y, 2))


def circunferencia(diamtero):
    """
    calcula la circunferencia usando el diametro de un circulo
    :param diamtero:
    :return: circunferencia
    """
    return diamtero * pi


def area_circle(diametro):
    """
    calcula la superficie del circulo
    :param diametro:
    :return:
    """
    return pi * pow(diametro, 2) / 4


def area_triangulo(base, altura):
    """
    calcula superficie del triangulo rectangulo
    :param base: base del triangulo
    :param altura: altura del triangulo
    :return:
    """
    return (base * altura) / 2


def angulo_alfa(base, altura):
    """
    retorna los angulos internos del triangulo rectangulo
    """
    alpha = atan(altura/base)
    beta = pi/2 - alpha
    return alpha, beta
