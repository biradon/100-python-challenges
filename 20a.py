def is_power_of_2(n):
    if n == 2:
        return True
    remainder = n // 2
    quotitent = n % 2
    if quotitent != 0:
        return False
    else:
        return is_power_of_2(remainder)

print(is_power_of_2(2))
print(is_power_of_2(10))
print(is_power_of_2(16))
print(is_power_of_2(1024))
print(is_power_of_2(1026))