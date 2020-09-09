# Librerias
from geometria_plana import area_circle, area_triangulo, hipotenusa, circunferencia, angulo_alfa

def main():
    """
    Programa Principal
    :return:
    """
    print("Programa Geometría Plana")

    x = float(input("Ingrese cateto x: "))
    y = float(input("Ingrese cateto y: "))

    hipot = hipotenusa(x=x, y=y)
    circunf = circunferencia(diamtero=hipot)
    area_circulo = area_circle(diametro=hipot)
    alpha, beta = angulo_alfa(base=x, altura=y)

    print("cateto {:.3f} y cateto {:.3f}, la hipotenusa es {:.3f}".format(x, y, hipot))
    print("area triangulo es {:.3f}".format(area_triangulo(base=x, altura=y)))
    print("los angulos internos del triangulo {:.3f}, {:.3f} son {:.3f} rad, {:.3f} rad3".format(x, y, alpha, beta))
    print("Area del circulo de diametro {:.3f} es: {:.3f}".format(hipot, area_circulo))
    print("Circuferencia del circulo de diametro {:.3f} es : {:.3f}".format(hipot, circunf))


if __name__ == '__main__':
    main()