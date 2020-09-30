import random
from functions import calCompas

noConsiderar = []
numeradores = {1: 2, 2: 3, 3: 4}
denominadores = {1: 2, 2: 4, 3: 8}

numeradorInput = input ("Ingrese el compas: ")
denominadorInput = input ("Ingrese la subdivision: ")
numerador = int(numeradorInput) if ("" != numeradorInput) else numeradores[random.choice(list(numeradores.keys()))]
denominador = int(denominadorInput) if ("" != denominadorInput) else denominadores[random.choice(list(denominadores.keys()))]

print ("Compas: {n}/{d}".format(n = numerador, d = denominador))

"""
    Menú de dictado: 
    Pide ingresar una opción para que empieze el dictado
    n: Sale del menú y termina el programa
    Otro: Imprime el dictado de compás
"""
opcion = ""
while (opcion != "n"):
    opcion = input("Presione enter para continuar y n para salir: ")
    if opcion != "": continue
    print ()
    [print(e,end=" ") for e in calCompas(numerador, noConsiderar)]
    print()
    print()
    # [print(random.choice([False, True]), end=", ") for x in range(numerador)]
    # print()








