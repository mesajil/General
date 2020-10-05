
def desplegarMenuPrincipal ():
    print ("Bienvenido, elija una opcion: ")
    print ("1. Dictado de notas musicales")
    print ("2. Dictado de letras del abecedario")
    print ("Presione n para salir")

op = ""

while (op != "n"):
    desplegarMenuPrincipal ()
    op = input()
    if (op != ""):
        continue


