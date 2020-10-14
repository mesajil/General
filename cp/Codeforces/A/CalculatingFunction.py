""" 
Se calcula f(n) = -1 + 2 -3 + .. + (-1)^n * n
"""

def function (n):
    k = int (n/2)
    p = int ((n + 1)/2)
    return k * (k + 1) - p * p


n = int (input ())
print (function(n))