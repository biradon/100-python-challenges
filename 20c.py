def power_of(value, exponent):
    result = value
    while exponent > 1:
        result *= value 
        exponent -= 1
    return result


print(power_of(4,3))
print(power_of(5,9))
print(power_of(10,4))
print(power_of(8,7))