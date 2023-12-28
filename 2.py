def number_as_text(n):
    result = " "
    while n > 0:
        last_number = n % 10
        text = convert_to_text(last_number)
        n = n // 10
        result =  text  + " " + result
    return result.strip()

def convert_to_text(n):
    if n == 1:
        return "ONE"
    if n == 2:
        return "TWO"
    if n == 3:
        return "THREE"
    if n == 4:
        return "FOUR"
    if n == 5:
        return "FIVE"
    if n == 6:
        return "SIX"
    if n == 7:
        return "SEVEN"
    if n == 8:
        return "EIGHT"
    if n == 9:
        return "NINE"
    if n == 0:
        return "ZERO"
    

print(number_as_text(789159456))
