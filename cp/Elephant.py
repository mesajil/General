def solve (x):
    return x//5 + (x%5 != 0)

x = int (input())

print (solve(x))