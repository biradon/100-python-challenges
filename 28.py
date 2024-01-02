def reverse(text):
    result = ""
    for i in range(len(text)):
        result += text[len(text) - 1 - i]
    return result

print(reverse("ABCD"))
print(reverse("OTTO"))
print(reverse("PETER"))