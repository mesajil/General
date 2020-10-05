def solve (s):
    ns = 0
    last = ""
    for c in s:
        if (last == c):
            ns += 1
        else:
            last = c
    return ns

n = int(input())
s = input()

print (solve(s))


