"""isprime_large"""
def isprime_large(number):
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
    if isprime_large(number):
        print("YES")
    else:
        print("NO")
main(int(input()))
