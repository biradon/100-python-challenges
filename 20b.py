def power_of(value, exponent):
    #base case
    if exponent == 1:
        return value
    #recursive case
    return power_of(value, exponent - 1) * value

print(power_of(4,3))
print(power_of(5,9))
print(power_of(10,4))
print(power_of(8,7))