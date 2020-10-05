import random
import string

def returnRandomLetters (n):
    str = ""
    for _ in range(n):
        str += random.choice(string.ascii_uppercase)
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
