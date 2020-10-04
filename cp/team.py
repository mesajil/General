



n = int(input ())
nProblemsToSolve = 0
for i in range (n):
    p,v,t = map(int, input().split())
    nProblemsToSolve += (1 if (p + v + t > 1) else 0)

print (nProblemsToSolve)