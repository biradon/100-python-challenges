# def print_it_out(n):
#     for row in range(1,n+1):
#         for col in range(1, row+1):
#             print(calc(row, col), end=" ")
#         print()

# def calc(row, col):
#     #base case
#     if col == 1 and row == 1:
#         return 1
#     if col == 1 or col == row:
#         return 1
#     #recursive case
#     return calc(row-1,col) + calc(row-1, col-1)

# print_it_out(5)

def calc_pascal_with_action(n):
    #base case 
    if n == 1:
        print([1])
        return [1]
    #recursive case
    else:
        previous_line = calc_pascal_with_action(n-1)
        new_line = calc_support(previous_line)
        print(new_line)
        return new_line

def calc_support(previous_line):
    current_line = []
    for i in range(len(previous_line)-1):
        current_line.append(previous_line[i] + previous_line[i+1])
    return [1] + current_line + [1]

calc_pascal_with_action(7)