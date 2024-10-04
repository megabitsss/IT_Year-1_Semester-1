"""is_prime_LARGER"""
def is_prime(n):
    """checking if the number is prime number"""
    if n <= 1: #Even nums won't be prime
        return "False"
    # if not n % 2:
    #     return "False"
    for divisor in range(3, int(n**0.5)+1, 2):
        if not n % divisor:
            return "False"
    return "True"
print(is_prime(int(input())))
