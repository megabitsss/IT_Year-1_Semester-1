"""heron of alexandria"""
import math
def area_finder(a, b, c):
    """find the area"""
    s = (a+b+c)/2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"{area:.3f}")
area_finder(float(input()), float(input()), float(input()))
