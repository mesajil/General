""" Encontrar el número de dólares a pedir prestado
si se desea comprar w bananas. Cada banana i cuesta k*i
 """

def solve(k,n,w):
    t = k*(w)*(w + 1)//2 - n
    return t*(t>=0)


k,n,w = map (int, input().split())


print (solve(k,n,w))