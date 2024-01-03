def capitalize(text):
    temp = list(text)
    for i in range(len(temp)):
        if i == 0:
            temp[i] = temp[i].upper()
        if temp[i] == " ":
            temp[i+1] = temp[i+1].upper()
    result = ''.join(temp)
    return result

print(capitalize("this is a very special title"))
print(capitalize("effective java is great"))


def modification(text):
    temp = " ".join(text)
    temp = list(temp)
    for i in range(len(temp)):
        if i == 0:
            temp[i] = temp[i].upper()
        if temp[i] == " ":
            temp[i+1] = temp[i+1].upper()
    result = ''.join(temp)
    final_result = result.split(' ')
    return final_result


# print(modification(["this","is","a","very","special","title"]))
# print(modification(["effective","java","is","great"]))

def special(text, ignorable_words):
    result = []
    for i in range(len(text)):
        if text[i] not in ignorable_words:
            clone = ""
            for j in range(len(text[i])):
                if j == 0:
                    clone += text[i][j].upper()
                else:
                    clone += text[i][j]
            result.append(clone)
        else:
            result.append(text[i])
    return result



print(special(["this","is","a","very","special","title"], ["is","a"]))