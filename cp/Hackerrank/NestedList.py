""" Retornar la lista de estudiantes que obtuvieron la segunda nota más baja.
La lista a devolver debe estar en orden asecendente """

def solve(l):
    l.sort(key = lambda e: e["score"])
    lastScore = l[0]["score"]
    s = []
    for i in range (1, len(l)):
        if (lastScore != l[i]["score"]):
            lastScore = l[i]["score"]
            s.append(l[i]["name"])
            for st in l[i+1:]:
                if (lastScore == st["score"]):
                    s.append(st["name"])
                else:
                    break
            break
    s.sort()
    return s




if __name__ == '__main__':
    n = int(input ())
    l = []
    for i in range(n):
        st = {}
        st["name"] = input()
        st["score"] = float(input())
        l.append(st)
    
    for i in solve(l):
        print (i)