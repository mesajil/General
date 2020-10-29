

def esPrimo(n):
    for i in range(2,n//2+1):
        if (n%i == 0):
            return False
    return True



if __name__ == "__main__":
    n = int(input("Ingrese numero de primos: "))

    for i in range (n):
        if esPrimo(i):
            print (i,end=", ")
    print()