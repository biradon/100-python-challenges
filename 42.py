def find_common(values1, values2):
    result = set()
    for i in range(len(values1)):
        for j in range(len(values2)):
            if values1[i] == values2[j]:
                result.add(values1[i])
    return result


print(find_common([1,2,4,7,8],[2,3,7,9]))
print(find_common([1,2,7,4,7,8],[7,7,3,2,9]))
print(find_common([2,4,6,8],[1,3,5,7,9]))