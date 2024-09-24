"""isprime_small"""
def isprime_small(number):
    """checking if nubmer is prime number"""
    if not number:
        return False
    if number == 1:
        return False
    if number == 2:
        return True
    for divisor in range(2, int(number**0.5)+2):
        if not number % divisor: #number % divisor == 0
            return False
    return True
def main(number):
    """main process of calculating"""
    if isprime_small(number):
        print("Yes")
    else:
        print("No")
main(int(input()))
