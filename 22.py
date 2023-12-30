def is_number_palindrome(number):
    array_of_digits = list(map(int, str(number)))
    left = 0
    right = len(array_of_digits) - 1
    return support(array_of_digits, left, right)

def support(number, left, right):
    #base case
    if left >= right:
        return True
    if number[left] != number[right]:
        return False
    #Recusive Case
    if  number[left] == number[right]:
        return support(number, left +1, right -1)
    

print(is_number_palindrome(7))
print(is_number_palindrome(13))
print(is_number_palindrome(171))
print(is_number_palindrome(47742))
    