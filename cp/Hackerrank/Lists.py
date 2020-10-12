OPERADORES = ["insert", "print", "remove" , "append", "sort" , "pop", "reverse"]


def solve(l, cmd, args):
    if (cmd == OPERADORES[0]):
        l.insert(args[0], args[1])
    elif (cmd == OPERADORES[1]):
        print(l)
    elif (cmd == OPERADORES[2]):
        l.remove(args[0])
    elif (cmd == OPERADORES[3]):
        l.append(args[0])
    elif (cmd == OPERADORES[4]):
        l.sort()
    elif (cmd == OPERADORES[5]):
        l.pop()
    elif (cmd == OPERADORES[6]):
        l.reverse()



if __name__ == '__main__':
    n = int(input ())
    l = []
    for _ in range (n):
        line = input().split()
        cmd = line[0]
        args = list(map(int, line[1:]))
        solve(l, cmd, args)
