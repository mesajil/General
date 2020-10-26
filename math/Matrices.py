import random
def printMatriz (matriz, f):
    n = len(matriz)
    m = len(matriz[0])
    diagonalMayor = []
    diagonalMenor = []
    for i in range(n):
        for j in range (m):
            e = f(i,j)
            print ("{:1d}".format(e), end=" ")
            if (i == j):
                diagonalMayor.append(e)
            if (i+j == n - 1):
                diagonalMenor.append(e)
        print()

    print("Diagonal mayor: {}".format(diagonalMayor))
    print("Diagonal menor: {}".format(diagonalMenor))
    print("Traza: {}".format(sum(diagonalMayor)))



if __name__ == "__main__":

    while (1):
        n = int (input("Matriz cuadrada: "))
        matriz = [[i + j for j in range (n)] for i in range(n)]
        printMatriz(matriz, lambda i,j: 1 if (i == j) else 0)