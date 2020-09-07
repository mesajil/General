import random
def baseOfSound (base, sonido):
    if base == 1:
        return sonido + sonido[-1]*2
    elif base == 2:
        return sonido
    elif base == 3:
        return sonido*2
    elif base == 4:
        return sonido*4

def compas(numerador, sonidos, noConsiderar):
    pulsos = []
    contador = 0
    bases = {1:2, 2:1, 3:1, 4:1}
    while (contador != numerador):
        sonido = random.choice(list(sonidos.keys()))
        if sonido in noConsiderar:
            continue
        else:
            base = random.choice(list(bases.keys()))
            if ((contador + bases[base])> numerador):
                continue
            else:
                contador += bases[base]
                pulsos.append(baseOfSound(base, sonidos[sonido]))
    return pulsos





sonidos = {1: ' DO', 2: ' RE', 3: ' MI', 4: ' FA', 5: 'SOL', 6: ' LA', 7: ' SI'}
noConsiderar = [7]
numeradores = {1: 2, 2: 3, 3: 4}
denominadores = {1: 2, 2: 4, 3: 8}
numerador = random.choice(list(numeradores.keys()))
denominador = random.choice(list(denominadores.keys()))

print ("Compas: {n}/{d}".format(n = numeradores[numerador], d = denominadores[denominador]))
salir = True

while (salir == True):
    opcion = input("Presione enter para continuar y n para salir: ")
    if opcion == 'n':
        salir = False
    elif opcion == '':
        pulsos = compas(numeradores[numerador], sonidos, noConsiderar)
        print(pulsos)
    else:
        continue
        