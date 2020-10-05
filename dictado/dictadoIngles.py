import random
import string
VOCALES = "AEIOU"
def returnRandomLetters (n):
    str = ""
    i = 0
    while (i < n):
        c = random.choice(string.ascii_uppercase)
        if (c == "U") or (c not in VOCALES):
            str += c
            i += 1 
    return str

def desplegarMenu ():
    print ("Presione enter para siguiente dictado, n para salir")


op = ""
print ("Ingrese numero de letras a generar: ")
n = int (input())

while (op != "n"):
    desplegarMenu ()
    op = input()
    if (op != ""):
        continue
    print (returnRandomLetters(n), "\n\n")
