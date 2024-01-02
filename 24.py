# def count_substrings(text, value_to_find):
#     #Base case
#     if len(text) < len(value_to_find):
#         return 0
#     #Recursive case
#     count = 0
#     remaining = ""

#     if text.startswith(value_to_find):
#         count = 1
#         remaining = text[len(value_to_find):]
#     else:
#         remaining = text[1:]
#     return count_substrings(remaining, value_to_find) + count

def count_substrings(text, value_to_find):
    return count_substrings_helper(text, value_to_find, 0)

def count_substrings_helper(text, value_to_find, left):
    #Base case 
    if len(text) - left < len(value_to_find):
        return 0
    
    count = 0
    if text.startswith(value_to_find, left):
        count = 1
        left += len(value_to_find)
    else:
        left +=1
    
    return count_substrings_helper(text, value_to_find, left) + count
    


print(count_substrings("xhixhix","x"))
print(count_substrings("xhixhix","hi"))
print(count_substrings("mic","mic"))
print(count_substrings("haha","ho"))
print(count_substrings("xxxxyz","xx"))




