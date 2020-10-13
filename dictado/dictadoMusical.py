
"""
    Menú de dictado: 
    Pide ingresar una opción para que empieze el dictado
    n: Sale del menú y termina el programa
    Otro: Imprime el dictado de compás
"""

import random
from functions import calCompas
import musicalSymbols
numeradores = {1: 2, 2: 3, 3: 4}
denominadores = {1: 2, 2: 4, 3: 8}
def desplegarMenu ():
    print ()
    print ("#  Menu de dictado musical:")
    print ("1. Presione enter o uno para imprimir el siguiente compas")
    print ("2. Para imprimir el resumen de compases dictados hasta el momento.")
    print ("   Presione r o dos y adicione el numero de columnas de la impresión")
    print ("   Ejemplo: 2 2")
    print ("n. Presione n para salir.")

def printCompases (cmd, compases):
    # cmd es de la forma ["r", "2"] o ["2", "2"]
    # cmd[1] representa el número de columnas, este puede variar dependiendo del número ingresado
    i = 0
    col = int (cmd[1])
    while (i < len(compases)):
        j = 0
        while (j < col and i < len(compases)):
            printCompas(compases[i])
            print("\t\t", end = " ")
            j += 1
            i += 1
        print ()

def printCompas(compas):
    [print(nota,end=" ") for nota in compas]
    if len(compas) == 1:
        print("\t", end = "")

numeradorInput = input ("Ingrese el compas: ")
denominadorInput = input ("Ingrese la subdivision: ")
numerador = int(numeradorInput) if ("" != numeradorInput) else numeradores[random.choice(list(numeradores.keys()))]
denominador = int(denominadorInput) if ("" != denominadorInput) else denominadores[random.choice(list(denominadores.keys()))]

print ("Compas: {n}/{d}".format(n = numerador, d = denominador))
op = ""
NOTAS = musicalSymbols.NOTAS_EN
compases = []
nCompas = 0
desplegarMenu()

while (op != "n"):
    print ("Presione enter para continuar, n para salir o r para imprimir resumen.")
    op = input()
    if (op == "" or op == "1"):
        compases.append(calCompas(numerador, NOTAS, False))
        printCompas(compases[nCompas])
        print("\n")
        nCompas += 1
    else:
        cmd = op.split()
        if (len(cmd) > 1 and (cmd[0] == "2" or cmd[0] == "r")):
            printCompases(cmd, compases)







