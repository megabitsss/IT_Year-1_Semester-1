"""Divide 3 or 5"""
def divide_3_or_5(n):
    """find number from 1 to n and return of each number that is divided by 3 or 5"""
    total = 0
    for i in range(1, n+1):
        if not i % 3 or not i % 5:
            total += i
    print(total)
divide_3_or_5(int(input()))
