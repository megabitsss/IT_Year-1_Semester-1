"""longer"""
import math
def longer_machine(radius, a, b):
    """circumference and perimeter"""
    circum = 2 * math.pi * radius
    perimeter = (a * 2) + (b*2)
    if circum > perimeter:
        print("Circle is longer")
    elif perimeter > circum:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f"{abs(perimeter-circum):.5f}")
longer_machine(float(input()), float(input()), float(input()))
