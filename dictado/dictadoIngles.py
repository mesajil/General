import random
import string

def returnRandomLetters (n):
    str = ""
    for _ in range(n):
        str += random.choice(string.ascii_uppercase)
    return str


