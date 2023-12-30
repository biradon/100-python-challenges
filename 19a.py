# def to_binary(n):
#     stored_value = []
#     return convert(n, stored_value)

# def convert(n, stored_value):
#     if n == 0:
#         final_result = "".join(list(reversed(stored_value)))
#         return final_result
#     quotient = n // 2
#     remainder = n % 2
#     stored_value.append(str(remainder))
#     return convert(quotient, stored_value)



def to_binary(n):
    #base case
    if n <= 1:
        return str(n)
    remainder = n // 2
    last_digit = n % 2
    #recursive case
    return to_binary(remainder) + str(last_digit)
    

print(to_binary(5))
print(to_binary(7))
print(to_binary(22))
print(to_binary(42))
print(to_binary(256))