import string
def generar_dicc (cadena):
    n = len(cadena)
    return {c: cadena[n - 1 - i] for i,c in enumerate(cadena)}


def solve (mensaje, dicc):
    return "".join([dicc[c] for c in mensaje])


if __name__ == "__main__":
    dicc = generar_dicc (string.printable)
    mensaje = input("Ingrese el mensaje: ")
    clave = input ("Igrese la clave: ")
    encriptado = solve (mensaje, dicc)
    print ("VER MENSAJE: ")
    while (1):
        if (clave == input ("Ingrese la clave: ")):
            print(solve(encriptado, dicc))
        else:
            print ("Clave incorrrecta: {}".format(encriptado))