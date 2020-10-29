import random

def startGame (n):
    contador = 0
    while (1):
        contador += 1
        myNumber = int(input("Ingresa tu numero: "))
        if (n == myNumber):
            print ("GANASTE !!!")
            break
        elif (myNumber > n):
            print ("Incorrecto :(, el numero a adivinar es MENOR !!")
        else:
            print ("Incorrecto :(, el numero a adivinar es MAYOR !!")
    print ("Te costo una cantidad de {} intentos".format(contador))


if __name__ == "__main__":
    n = int(input("Ingrese rango de numeros: "))
    startGame (random.randint(0,n))