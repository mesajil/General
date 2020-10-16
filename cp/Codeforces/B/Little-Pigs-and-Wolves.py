"""
# Solución utilizando recursividad
def solve(grid):
    
    n = len(grid)
    m = len(grid[0])
    s = [0]
    # nWolves = sum([1 for i in range(n) for j in range(m) if grid[i][j] == "W"])
    for i in range(n):
        for j in range (m):
            if grid[i][j] == 'W':
                # Si es lobo, verificar los 4 casos posibles: arriba, izq, der, abajo
                for p in range(-1,2):
                    for q in range(-1,2):
                        if (abs(p + q) == 1 and i + p < n and i + p >= 0 and j + q < m and j + q >= 0 and grid[i + p][j + q] == "P"):
                            grid[i][j] = "."
                            grid[i + p][j + q] = "."
                            s.append(1 + solve (grid.copy()))
                            grid[i][j] = "W"
                            grid[i + p][j + q] = "P"
                            
                
    return max(s)
"""
def isAdjacent (grid, i, j, cell):
    for p in range(-1,2):
        for q in range(-1,2):
            if (abs(p + q) == 1 and i + p < n and i + p >= 0 and j + q < m and j + q >= 0 and grid[i + p][j + q] == cell):
                return True
    return False
                            
def solve (grid):
    n = len(grid)
    m = len(grid[0])
    nWolves = 0
    nPigs = 0
    for i in range (n):
        for j in range (m):
            if (grid[i][j] == "W" and isAdjacent(grid, i, j, "P")):
                nWolves += 1
            elif (grid[i][j] == "P" and isAdjacent(grid, i, j, "W")):
                nPigs += 1
    return min(nWolves, nPigs)


if __name__ == "__main__":
    n, m = map (int, input ().split())

    grid = []
    for _ in range (n):
        grid.append ([c for c in input()])
    print (solve(grid))



    