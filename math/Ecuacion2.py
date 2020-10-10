from math import sqrt
def ecuacion (x):
    return pow(x,5) + pow(x,4) + 1

def xGrado3 (p,q):
    a = -q/2
    b = sqrt(pow(q,2)/4 + pow(p,3)/27)
    return ((a + b) ** 1/3) + ((a - b) ** 1/3)
g = xGrado3(-1,1)
print (g)
print (ecuacion(g))

