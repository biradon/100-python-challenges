from collections import defaultdict 


def check_no_duplicae_cahrds(text):
    map_value = defaultdict(lambda: 0)
    text = text.lower()
    for char in text:
        map_value[char] +=1
        if map_value[char] > 1:
            return False

    return True

print(check_no_duplicae_cahrds("Otto"))
print(check_no_duplicae_cahrds("Adrian"))
print(check_no_duplicae_cahrds("Micha"))
print(check_no_duplicae_cahrds("ABCDEFG"))