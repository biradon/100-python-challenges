def calc_checksum(digits):
    sum = 0
    for i in range(0, len(digits)):
        sum += (i+1) * int(digits[i])
    result = sum % 10
    return result

print(calc_checksum("87654321"))