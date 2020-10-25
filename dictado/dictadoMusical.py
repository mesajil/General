
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
    print ("   Presione r o dos y adicione el numero de columnas de la impresion")
    print ("   Ejemplo: 2 2")
    print ("n. Presione n para salir.")

def printCompases (col, compases):
    i = 0
    while (i < len(compases)):
        j = 0
        while (j < col and i < len(compases)):
            printCompas(compases[i], 1, " ")
            print("\t", end = " ")
            j += 1
            i += 1
        print ()

def printCompas(compas, mode = 0, sep = '\t', car = "*"):
    
    if mode == 0:
        for (altura, ritmo) in compas:
            if altura:
                print(ritmo,end=sep)
            else:
                print(car,end=sep)
        print()
        for (altura, ritmo) in compas:
            if not altura:
                print(ritmo,end=sep)
            else:
                print(car,end=sep)
    elif mode == 1:
        [print(("|" if (altura) else "")+ritmo,end=sep) for (altura, ritmo) in compas]

desplegarMenu()
numeradorInput = input ("Ingrese el compas: ")
denominadorInput = input ("Ingrese la subdivision: ")
numerador = int(numeradorInput) if ("" != numeradorInput) else numeradores[random.choice(list(numeradores.keys()))]
denominador = int(denominadorInput) if ("" != denominadorInput) else denominadores[random.choice(list(denominadores.keys()))]

print ("Compas: {n}/{d}".format(n = numerador, d = denominador))
op = ""
NOTAS = musicalSymbols.NOTAS_EN
compases = []
nCompas = 0

while (op != "n"):
    print ("Presione enter para continuar, n para salir o r para imprimir resumen.")
    op = input()
    if (op == "" or op == "1"):
        compases.append(calCompas(numerador, NOTAS))
        printCompas(compases[nCompas])
        print("\n")
        nCompas += 1
    else:
        cmd = op.split()
        if (len(cmd) > 1 and (int(cmd[0])%2 == 0 or cmd[0] == "r")):
            printCompases(int(cmd[1]), compases)







