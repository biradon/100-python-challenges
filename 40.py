def str_to_number(text):
    map_value = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0
    }
    result = []
    final_result = 0
    operator = 0
    for i in range(len(text)):
        if text[i].isalpha():
            return "ValueError"
        if text[i] == "-":
            operator = -1
            continue
        if text[i] == "+":
            operator = 1
            continue
        result.append(map_value[text[i]])
    
    for i in range(len(result)):
        final_result += result[i] * 10 ** (len(result) - 1 - i)
    final_result *= operator
    return final_result


print(str_to_number("+123"))
print(str_to_number("-123"))
print(str_to_number("7271"))
print(str_to_number("ABC"))




