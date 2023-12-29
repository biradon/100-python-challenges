result = []
a = 256

while a > 0:
    quotient = a // 2
    remainder = a % 2
    a = quotient
    result.append(str(remainder))

final_result = "".join(list(reversed(result)))
print(final_result)