import math 

def lcm(a,b):
    result = a * b // math.gcd(a, b)
    return result


print(lcm(42,14))