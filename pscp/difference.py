"""Difference"""
def set_difference(n, m):
    """Find A-B set"""
    a = set()
    b = set()
    for _ in range(n):
        a.add(int(input()))
    for _ in range(m):
        b.add(int(input()))
    for number in sorted(a-b):
        print(number, end=" ")
set_difference(int(input()), int(input()))
