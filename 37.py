def matches_pattern(pattern, text):
    text = text.split(" ")
    map_value = {}
    if len(pattern) == len(text):
        for i in range(len(pattern)):
            if pattern[i] not in map_value:
                map_value[pattern[i]] = text[i]
            else:
                if map_value[pattern[i]] != text[i]:
                    return False
    return True



print(matches_pattern("xyyx","tim mike mike tim"))
print(matches_pattern("xyyx","tim mike tom tim"))
print(matches_pattern("xyxx","tim mike mike tim"))
print(matches_pattern("xxxx","tim tim tim tim"))