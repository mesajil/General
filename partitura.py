import random
ns = int (input ("Número de sistemas: "))

col = 6
simbolos = [" QN", " HN", " WN", "2EN", "4SN"]
silencios = [' WR', ' HR', ' QR', ' ER', ' SR']
sinSonido = ' - '
sonidos = ['SOL', ' MI']


for i in range(ns):
    for j in range(col):
        simbolo = random.choice(simbolos + silencios)
        sonido = sinSonido if simbolo in silencios else random.choice (sonidos)
        formato = '{i}{j}: {simbolo}|{sonido}'.format(i=i+1, j=j+1, simbolo = simbolo, sonido = sonido)
        print(formato, end = ", ")
    print ()
