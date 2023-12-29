def reverse_string(text):
    left = 0
    right = len(text) - 1
    array = list(text)
    return convert(array, left, right)


def convert(text, left, right):
    if left >= right:
        result = ''.join(text)
        return result
    temp = text[left]
    text[left] = text[right]
    text[right] = temp
    return convert(text, left + 1, right -1)





print(reverse_string("abcdefghi"))