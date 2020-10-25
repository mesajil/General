import random
from musicalSymbols import REST

def formatSound (base, pair, puntillo):
    if base == 1: return '*' + pair[0] + '*' + ("." if puntillo else "")
    if base == 2: return pair[0]
    if base == 3: return pair[0] + pair[1]
    if base == 4: return pair[0]*2 + pair[1]*2



def calCompas(numerador, NOTAS):
    pulsos = []
    contador = 0
    bases = {1:2, 2:1, 3:1, 4:1}
    while (contador != numerador):
        sonido = random.choice(list(NOTAS.keys()))
        
        base = random.choice(list(bases.keys())) if NOTAS[sonido] != REST else 2

        if ((contador + bases[base])> numerador): continue
        
        contador += bases[base]

        puntillo = False
        if (base == 1):
            if (random.choice([True, False])):
                if ((contador + 1) <= numerador):
                    puntillo = True
                    contador += 1
        
        sonido2 = REST
        if (base == 3 or base == 4):
            while (sonido2 == REST):
                sonido2 = NOTAS[random.choice(list(NOTAS.keys()))]
        
        altura = random.choice(range(2))
        ritmo = formatSound(base, (NOTAS[sonido], sonido2), puntillo)
        pulsos.append((altura, ritmo))

    return pulsos



