def contains_rotation(str1, str2):
    new_doubled_str1 = (str1 + str1).lower()
    return str2.lower() in new_doubled_str1

print(contains_rotation("ABCDEF", "EFAB"))

