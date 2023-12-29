def sum_rec(values):
    return sum_support(values, 0)

def sum_support(values, pos):
    #base case
    if pos >= len(values):
        return 0
    #Recursion case
    return values[pos] + sum_support(values, pos + 1)


def sum_rerversed(values):
    return sum_support1(values, len(values) - 1)

def sum_support1(values, pos):
    if pos < 0:
        return 0
    return values[pos] + sum_support1(values, pos - 1)

print(sum_rerversed([1,2,3,-7]))