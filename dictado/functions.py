from constans import NOTAS
import random

# def verSiEsInvertida (pair):

def formatSound (base, pair, puntillo):
    if base == 1: return '(' + pair[0] + ')' + ("." if puntillo else "")
    if base == 2: return pair[0]
    if base == 3: return pair[0] + pair[1]
    if base == 4: return pair[0]*2 + pair[1]*2



def calCompas(numerador, noConsiderar):
    pulsos = []
    contador = 0
    bases = {1:2, 2:1, 3:1, 4:1}
    while (contador != numerador):
        sonido = random.choice(list(NOTAS.keys()))
        
        if sonido in noConsiderar: continue
        base = random.choice(list(bases.keys())) if sonido != 8 else 2

        if ((contador + bases[base])> numerador): continue
        
        contador += bases[base]

        puntillo = False
        if (base == 1):
            if (random.choice([True, False])):
                if ((contador + 1) <= numerador):
                    puntillo = True
                    contador += 1
        
        sonido2 = 8
        if (base == 3 or base == 4):
            while (sonido2 == 8):
                sonido2 = random.choice(list(NOTAS.keys()))

        pulsos.append(formatSound(base, (NOTAS[sonido], NOTAS[sonido2]), puntillo))

    return pulsos