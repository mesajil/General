
def solve3(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            count += 1
    return count

def solve2 (s, sub):
    count = 0
    while sub in s:
        i = s.index(sub)
        s = s[i+1:]
        count += 1
    return count


def solve1 (s,sub):
    count = 0
    for i in range (len(s)):
        count += s[i:].startswith(sub)
    return count


def solve (s,sub):
    return sum([1 for i in range(len(s)) if s[i:i+len(sub)] == sub])

if __name__ == "__main__":
    s = input()
    sub = input()
    print (solve3(s, sub))