"""game"""
def tie_checker(a, b):
    """checker amount of ties in game or error"""
    a_mod = a % 3
    b_mod = b % 3
    if a_mod == b_mod:
        print(a_mod)
    else:
        print("Error")
tie_checker(int(input()), int(input()))
