

def countProblemsToSolve (n):
    ns = 0
    for i in range (n):
        p,v,t = map(int, input().split())
        ns += (p + v + t > 1)
    return ns


n = int(input ())

print (countProblemsToSolve(n))