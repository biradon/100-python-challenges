def from_roman_number(roman_number):
    last_digit = 0
    final_result = 0
    for character in reversed(roman_number):
        digit = map_value[character]
        compare = digit >= last_digit
        if compare:
            final_result+=digit
            last_digit = digit
        else:
            final_result-=digit
    return final_result

map_value = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


print(from_roman_number("XVII"))
print(from_roman_number("CDXLIV"))
print(from_roman_number("MCMLXXI"))
print(from_roman_number("MMXX"))