def solveDuplicate (lista):
    for i,x in enumerate(lista):
        for _,y in enumerate(lista[i+1:]):
            if (x == y):
                return x
    return -1
lista = [1,2,5,4,3,1]

print(solveDuplicate(lista))