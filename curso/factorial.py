def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


def funcion (n):
    return factorial(n+1)*factorial(n)/factorial(n - 1)*factorial(n)


n = int (input("n: "))
print (funcion(n))