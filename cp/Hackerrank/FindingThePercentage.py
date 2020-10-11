
def solve(marks, query):
    scores = marks[query]
    return sum(scores) / len(scores)



if __name__ == '__main__':
    n = int(input ())
    marks = {}
    for i in range(n):
        name, *line = input().split()
        marks[name] = list(map(float, line))
    query = input()

    print ("{:.2f}".format(solve(marks, query)))