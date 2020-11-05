
def bsearch (l, e):
    rango = (0,len(l)-1)
    while (1):
        if (rango[0]>rango[1]):
            break
        i = (rango[0] + rango[1])//2
        if (e == l[i]):
            return i
        elif (e > l[i]):
            rango = (i+1,rango[1])
        else:
            rango = (rango[0], i-1)
    return -1
if __name__ == "__main__":
    l = [1,2,6,2,4,6,7,8,8,1,11,2,3,4]
    l.sort()
    while (1):
        print (l)
        e = int (input("Ingresa elemento a buscar: "))
        print(bsearch (l,e))