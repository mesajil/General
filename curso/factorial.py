def solve(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


if __name__ == "__main__":
    while (1):
        n = int (input("Ingrese numero: "))
        print (solve(n))