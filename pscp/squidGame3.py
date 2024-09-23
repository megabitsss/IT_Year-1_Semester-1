"""Squid Game 3 - Tug-of-War"""
def death_finder():
    """find whether team a or team b is all dead"""
    a = 0
    b = 0
    for _ in range(10):
        a += int(input())
    for _ in range(10):
        b += int(input())
    if a < b:
        print("A")
    elif b < a:
        print("B")
    else:
        print("AB")
death_finder()
