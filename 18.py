def min_rec(values):
    return min_support(values, 0, 0)

def min_support(values, pos, index_of_min):
    #base case
    if pos >= len(values):
        return values[index_of_min]
    
    if values[pos] < values[index_of_min]:
        index_of_min = pos

    #recursion case
    return min_support(values, pos + 1, index_of_min)

print(min_rec([7, 2, 1, 9, 7, 1]))
print(min_rec([11, 2, 33, 44, 55, 6, 7]))
print(min_rec([1, 2, 3, -7]))