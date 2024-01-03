def to_morse_code(text):
    text = text.upper()
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:            
            result += morse_code_dict[char] + " "
    return result



morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

print(to_morse_code("E"))
print(to_morse_code("0"))
print(to_morse_code("S"))
print(to_morse_code("T"))
print(to_morse_code("W"))
print(to_morse_code("SOS"))
print(to_morse_code("TWEET"))
print(to_morse_code("WEST"))