def check_braces(text):
    result = [False] * (len(text))
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i] == "("  and text[j] == ")":
                if result[i] == False and result[j] == False:
                    result[i] = True
                    result[j] = True
    for i in range(len(result)):
        if result[i] == False:
            return False
    return True

print(check_braces("(())"))
print(check_braces("()()"))
print(check_braces("(()))(())"))
print(check_braces("((()"))
print(check_braces("))(("))



