""" Retorna, a partir de un conjunto l,
todos los subconjuntos en el que la suma de sus elementos es igual a un "n" dado """

def solve(l,n):
    if (l == []): return []
    s = []
    if (l[0] == n): s.append([l[0]])
    s.extend(solve(l[1:], n))
    s.extend([[l[0]] + p for p in solve(l[1:], n - l[0])])

    return s


l = [+1,-3,+7,-4,-2,-7,+9,-3,-5,-1,-8]
# l = [0,0,0]
# l = [0,1,1]
n = 1
print (solve(l,n))