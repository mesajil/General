import random
def formatSound (base, pair):
    if base == 1: return '(' + pair[0] + ')'
    if base == 2: return pair[0]
    if base == 3: return pair[0] + pair[1]
    if base == 4: return pair[0]*2 + pair[1]*2


def calCompas(numerador, sonidos, noConsiderar):
    pulsos = []
    contador = 0
    bases = {1:2, 2:1, 3:1, 4:1}
    while (contador != numerador):
        sonido = random.choice(list(sonidos.keys()))
        
        if sonido in noConsiderar: continue
        base = random.choice(list(bases.keys())) if sonido != 8 else 2
        if ((contador + bases[base])> numerador): continue
        
        sonido2 = 8
        if (base == 3 or base == 4):
            while (sonido2 == 8):
                sonido2 = random.choice(list(sonidos.keys()))

        contador += bases[base]
        pulsos.append(formatSound(base, (sonidos[sonido], sonidos[sonido2])))

    return pulsos





sonidos = {1: 'Do', 2: 'Re', 3: 'Mi', 4: 'Fa', 5: 'Sol', 6: 'La', 7: 'Si', 8: '()'}
noConsiderar = []
numeradores = {1: 2, 2: 3, 3: 4}
denominadores = {1: 2, 2: 4, 3: 8}

numeradorInput = input ("Ingrese el compas: ")
denominadorInput = input ("Ingrese la subdivision: ")
numerador = int(numeradorInput) if ("" != numeradorInput) else numeradores[random.choice(list(numeradores.keys()))]
denominador = int(denominadorInput) if ("" != denominadorInput) else denominadores[random.choice(list(denominadores.keys()))]

print ("Compas: {n}/{d}".format(n = numerador, d = denominador))
salir = True

"""
    Menú de dictado: 
    Pide ingresar una opción para que empieze el dictado
    n: Sale del menú y termina el programa
    Otro: Imprime el dictado de compás
"""
opcion = ""
while (opcion != "n"):
    opcion = input("Presione enter para continuar y n para salir: ")
    if opcion == 'n': continue
    
    [print(e,end=", ") for e in calCompas(numerador, sonidos, noConsiderar)]
    print()
    [print(random.choice([False, True]), end=", ") for x in range(numerador)]
    print()
