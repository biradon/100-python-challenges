def calc_sum_of_digits(value):
    if value == 1:
        result.append(value % 10)
        return sum(result)
    result.append(value % 10)
    return calc_sum_of_digits(value // 10)


result = []
print(calc_sum_of_digits(1234567))

