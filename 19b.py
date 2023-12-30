def to_octal(n):
    #base case
    if n <= 8:
        return str(n)
    remainder, last_digit = divmod(n, 8)
    return to_octal(remainder) + str(last_digit)

def to_hex(n):
    #base case
    if n < 16:
        if n > 10:
            return map_value[n]
        else:
            return str(n)
    remainder = n // 16
    if n % 16 > 10:
        last_digit = map_value[n%16]
    else:
        last_digit = n % 16

    return to_hex(remainder) + str(last_digit)

map_value = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}


print(to_octal(7))
print(to_octal(8))
print(to_octal(42))
print(to_hex(15))
print(to_hex(77))
print(to_hex(155))