import numpy as np


def f1(xs):
    return 8 * np.exp(- 2 * np.power((xs - 2), 2)) + (2 * xs + 1) + 3 * np.tanh(3 * xs + 2)


def f2(xs):
    return 2 * np.exp(- 2 * np.power((xs - 1), 2)) - np.exp(- np.power((xs - 1), 2))


def f3(xs):
    return np.sqrt(xs)


def f4(xs):
    return np.exp(- xs) * np.sin(2 * xs)


def main(f, interval, num):
    x0 = np.linspace(interval[0], interval[1], num)
    response = f(x0)

    # Nombre del archivo de salida
    archivo_salida = f.__name__ + "_train.txt"

    # Abrir el archivo en modo escritura
    with open(archivo_salida, 'w') as archivo:
        # Escribir las cabeceras de las columnas
        archivo.write("x0\tresponse\n")

        # Escribir los datos en las columnas
        for x, y in zip(x0, response):
            archivo.write(f"{x}\t{y}\n")

    print("Datos guardados en el archivo:", archivo_salida)


if __name__ == '__main__':
    f = f1
    interval = [-2, 4]
    num = 61
    main(f, interval, num)

    f = f2
    interval = [-1, 3]
    num = 41
    main(f, interval, num)

    f = f3
    interval = [0, 4]
    num = 41
    main(f, interval, num)

    f = f4
    interval = [0, 4]
    num = 41
    main(f, interval, num)


