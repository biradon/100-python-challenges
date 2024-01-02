def join(values, delimiter):
    result = ""
    for i in range(len(values)):
        if i == len(values) - 1:
            result += values[i]
        else:
            result += values[i] + delimiter
    return result


print(join(["hello", "world", "message"], "+++"))
        