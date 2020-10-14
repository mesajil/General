""" 
Entradas
n = 1   ->  I hate it
n = 2   ->  I hate that I love it
n = 3   ->  I hate that I love that I hate it
 """

def solve (n):
    for i in range (n):
        if i%2 == 0:
            print("I hate ", end = "")
        else:
            print("I love ", end = "")
        if i + 1 < n:
            print ("that ", end = "")
    print ("it")



n = int (input ())

solve(n)