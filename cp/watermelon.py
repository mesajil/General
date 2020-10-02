
def canDivideIntoTwoEvenNumbers (w):
    return "YES" if (w%2 == 0 and (w/2)%2 != 0 and (w/2) > 1) or (w%2 == 0 and (w/2)%2 == 0 and (w/2) > 0) else "NO"


w = int(input ())

print (canDivideIntoTwoEvenNumbers(w))