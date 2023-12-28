# from itertools import combinations

# def calc_max_possible_change(values):
#     final_results = 0
#     max_sum = sum(values)
#     results = [False] * max_sum

#     # Include individual values
#     for val in values:
#         results[val - 1] = True

#     # Include combinations of values
#     for r in range(2, len(values) + 1):
#         for combo in combinations(values, r):
#             results[sum(combo) - 1] = True

#     for i in range(0, len(results)):
#         if results[i]:
#             final_results+=1
#         else:
#             break

#     return final_results





def calc_max_possible_change(values):
    # wrappng / copying necessary so that we do not sort the original
    sorted_numbers = list(values)
    sorted_numbers.sort()
    max_possible_change = 0
    for current_value in sorted_numbers:
        if current_value > max_possible_change + 1:
            break
        max_possible_change += current_value
    return max_possible_change

array = [1, 1, 1]
print(calc_max_possible_change(array))