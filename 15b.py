def gcd(a,b):
    while b > 0:
        c = a
        a = b
        b = c % b
    return a

print(gcd(42,28))