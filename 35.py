from collections import defaultdict

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    map1 = set()
    map2 = set()
    for i in range(len(str1)):
        map1.add(str1[i])
    for j in range(len(str2)):
        map2.add(str2[j])
    if map1 == map2:
        return True
    else:
        return False
    

print(is_anagram("Otto","Toto"))
print(is_anagram("Mary","Army"))
print(is_anagram("Ananas","Bananas"))