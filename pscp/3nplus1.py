"""3nPlus1"""
def find_1():
    """repeat the loop till the number is 1"""
    while True:
        cnt = 1 #included 1 (final number in the sequence)
        number = int(input())
        if not number:
            break
        while number != 1:
            if not number % 2: #even
                number /= 2
            else: #odd
                number = number * 3 + 1
            cnt += 1
        print(cnt)
find_1()
