def calc_perfect_numbers(max_exclusive):
    sum = 0
    result = []
    for i in range(1, max_exclusive):
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            result.append(sum)
        sum = 0
    return result

print(calc_perfect_numbers(10000))