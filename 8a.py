import math

def solve_quadratic():
    for a in range(1, 100):
        for b in range(1, 100):
            c = int(math.sqrt(a * a + b * b))
            if a * a + b * b == c * c:
                print("a =", a, "/ b =", b, "/ c =", c)


solve_quadratic()