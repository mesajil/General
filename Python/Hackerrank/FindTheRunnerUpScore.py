
""" Econtrar el segundo mejor puntaje en conjunto de
puntajes "a" """

def solve(a):
    a.sort(reverse=True)
    last = a[0]
    for i in range (1, len(a)):
        if a[i] != last:
            return a[i]


if __name__ == '__main__':
    n = int(input ())
    a = list(map(int, input().split()))
    print (solve(a))