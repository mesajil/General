import random
import string

def solve(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])

if __name__ == "__main__":
    n = int(input())

    print (solve(n))