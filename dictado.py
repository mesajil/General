import random
def baseOfSound (base, sonido):
    if base == 1: return '(' + sonido + ')'
    if base == 2: return sonido
    if base == 3: return sonido*2
    if base == 4: return sonido*4


def calCompas(numerador, sonidos, noConsiderar):
    pulsos = []
    contador = 0
    bases = {1:2, 2:1, 3:1, 4:1}
    while (contador != numerador):
        sonido = random.choice(list(sonidos.keys()))
        if sonido in noConsiderar:
            continue
        else:
            base = random.choice(list(bases.keys())) if sonido != 8 else 2
            if ((contador + bases[base])> numerador):
                continue
            else:
                contador += bases[base]
                pulsos.append(baseOfSound(base, sonidos[sonido]))
    return pulsos





sonidos = {1: 'Do', 2: 'Re', 3: 'Mi', 4: 'Fa', 5: 'Sol', 6: 'La', 7: 'Si', 8: '{}'}
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
    Enter: Siguiente dictado de compás
    n: Salir del menú
    Other: Preguntar otra vez
"""
while (salir == True):
    opcion = input("Presione enter para continuar y n para salir: ")
    if opcion == 'n':
        salir = False
    elif opcion == '':
        pulsos = calCompas(numerador, sonidos, noConsiderar)
        print(pulsos)
    else:
        continue
        