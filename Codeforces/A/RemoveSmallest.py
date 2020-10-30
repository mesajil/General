"""
  ____          _      _____                       
 / ___|___   __| | ___|  ___|__  _ __ ___ ___  ___ 
| |   / _ \ / _` |/ _ \ |_ / _ \| '__/ __/ _ \/ __|
| |__| (_) | (_| |  __/  _| (_) | | | (_|  __/\__ \
 \____\___/ \__,_|\___|_|  \___/|_|  \___\___||___/


Encontrar si es posible obtener un arreglo de un elemento aplicando idefinidamente la siguiente operación:
Tomar 2 elementos del arreglo, los cuales tengan su diferencia absoluta igual o menor a uno, y eliminar el menor.
"""



def solve(a):
    a.sort()
    k = 0
    for i in range(len(a) - 1):
        if (a[i + 1] - a[i] <= 1):
            k += 1
        else:
            break
    return "YES" if len(a) - k == 1 else "NO"


if __name__ == "__main__":
    n = int (input ())
    arrays = []
    for _ in range (n):
        input ()
        arrays.append(list(map(int, input().split())))
    
    for i in range (n):
        print (solve(arrays[i]))