def calc_friends(max_exclusive):
    total = []
    for i in range(1, max_exclusive // 2 + 1):
        if max_exclusive % i == 0:
            total.append(i)

    return sum(total)



print(calc_friends(220))
print(calc_friends(284))
print(calc_friends(1184))
print(calc_friends(1210))
