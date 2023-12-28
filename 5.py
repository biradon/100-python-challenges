def calc_primes_up_to(max_value):
    is_potentially_prime = [True for _ in range(1, max_value)]

    for number in range(2, max_value // 2 + 1):
        if is_potentially_prime[number]:
            check_prime(number, is_potentially_prime)
    return convert_to_number(is_potentially_prime)

def check_prime(number, array):
    for i in range(number + number, len(array), number):
        array[i] = False



def convert_to_number(array):
    result = []
    for i in range(2, len(array)):
        if array[i] is True:
            result.append(i)
    return result
        
n = 50
twin = {}
cousin = {}
sexy = {}

for i in range(0, 50):
    if i in calc_primes_up_to(n) and i+2 in calc_primes_up_to(n+2):
        twin.update({i:i+2})

for i in range(0, 50):
    if i in calc_primes_up_to(n) and i+4 in calc_primes_up_to(n+4):
        cousin.update({i:i+4})

for i in range(0, 50):
    if i in calc_primes_up_to(n) and i+6 in calc_primes_up_to(n+6):
        sexy.update({i:i+6})

print(twin)
print(cousin)
print(sexy)