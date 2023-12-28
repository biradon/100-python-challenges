def from_decimal_number(decimal_number):
    reaminder = decimal_number
    result = ""
    for number in sorted(map_value.keys(), reverse=True):
        if reaminder > 0:
            roman_digit = map_value[number]
            times = reaminder // number
            reaminder = reaminder % number
            result += roman_digit * times
    return result


map_value = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
 40: "XL", 50: "L", 90: "XC", 100: "C",
400: "CD", 500: "D", 900: "CM", 1000: "M"}


print(from_decimal_number(17))
print(from_decimal_number(444))
print(from_decimal_number(1971))
print(from_decimal_number(2020))