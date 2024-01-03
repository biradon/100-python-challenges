from collections import defaultdict

def remove_duplicates(text):
    map_value = defaultdict(lambda: 0)
    result = ""
    for char in text:
        temp = char.lower()
        if map_value[temp] == 0:
            map_value[temp] += 1
            result += char
    return result


print(remove_duplicates("bananas"))
print(remove_duplicates("lalalamama"))
print(remove_duplicates("MICHAEL"))
print(remove_duplicates("AaBbcCdD"))