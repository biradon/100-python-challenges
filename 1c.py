def is_even(number):
    if number % 2 == 0:
        return True

def is_odd(number):
    if number % 2 != 0:
        return True
    
number = 6

if is_even(number):
    print("This is even number")
elif is_odd(number):
    print("This is odd number")