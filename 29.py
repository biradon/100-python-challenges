def is_palindrome(text):
    text = convert(text)
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i].lower() == text[len(text)-1-i].lower():
            continue
        else:
            return False
    return True

def convert(text):
    step1 = text.split()
    step2 = "".join(step1)
    for i in range(len(step2)):
        if not step2[i].isalpha():
            step2 = step2.replace(step2[i], "")
    return step2


print(is_palindrome("Otto"))
print(is_palindrome("ABCBX"))
print(is_palindrome("ABCXcba"))
print(is_palindrome("Was it a car or a cat I saw"))

