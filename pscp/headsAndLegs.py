"""Heads and Legs"""
def heads_legs(a, b):
    """find the amount of rabbit and bird"""
    bird = (4*a - b) / 2
    rabbit = (-2*a + b) / 2
    if min(bird, rabbit) < 0:
        print("Impossible")
    else:
        print(int(rabbit), int(bird))
heads_legs(int(input()), int(input()))
