def is_binary_number(values):
    for i in range(len(values)):
        if values[i] != "0" and values[i] != "1":
            return False
    return True


print(is_binary_number("101010"))


def to_decimal(values):
    sum = 0
    for i in range(len(values)):
        sum += int(values[i]) * (2**(len(values) - 1 - i))
    return sum

print(to_decimal("101010101010"))


def hex_to_decimal(values):
    sum = 0
    for i in range(len(values)):
        if values[i].isalpha():
            sum+= map_value[values[i]] * (16**(len(values) - 1 - i))
        else:
            sum+= int(values[i]) * (16**(len(values) - 1 - i))
    return sum


map_value = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


print(hex_to_decimal("ABC"))