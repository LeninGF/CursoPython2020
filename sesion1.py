# Librerias
from math import pi, pow, sqrt


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


def main():
    """
    Programa Principal
    :return:
    """
    print("Programa Geometría Plana")

    x = 3
    y = 4

    hipot = hipotenusa(x=x, y=y)
    circunf = circunferencia(diamtero=hipot)
    area_circulo = area_circle(diametro=hipot)

    print("cateto {:.3f} y cateto {:.3f}, la hipotenusa es {:.3f}".format(x, y, hipot))
    print("area triangulo es {:.3f}".format(area_triangulo(base=x, altura=y)))
    print("Area del circulo de diametro {:.3f} es: {:.3f}".format(hipot, area_circulo))
    print("Circuferencia del circulo de diametro {:.3f} es : {:.3f}".format(hipot, circunf))


if __name__ == '__main__':
    main()