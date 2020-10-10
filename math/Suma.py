

def solve(l,n):
    if (len(l) == 0):
        return []
    if (len(l) == 1):
        if l[0] == n:
            return [[n]]
        else:
            return []

    s = []
    for i,e in enumerate(l):
        ps = solve(l[i+1:], n - e)
        s.extend([[e] + p for p in ps])

    return s


# l = [+1,-3,+7,-4,-2,-7,+9,-3,-5,-1,-8]
l = [+1,0,-1]
n = 0
print (solve(l,n))