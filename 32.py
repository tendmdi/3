
import math

def x(n):
    result = 3
    for _ in range(n):
        result = math.sqrt(3 + result)
    return result

def x_rec(n, value=3):
    if n == 0:
        return value
    else:
        return x_rec(n-1, math.sqrt(3 + value))

print(x_rec(2), x(2)) 
