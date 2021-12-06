
def solve (tram):
    max = 0
    total = 0
    for a,b in tram:
        total += b - a
        if (total > max):
            max = total
    return max 


if __name__ == "__main__":
    
    n = int (input ())
    tram = []
    for _ in range (n):
        tram.append (list(map(int, input().split())))
    print (solve(tram))