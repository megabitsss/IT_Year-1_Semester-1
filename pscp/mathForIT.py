"""mathForIT"""
import math
def main(radius):
    """main func"""
    area = math.pi * (radius**2)
    circum = 2 * math.pi * radius
    print(f"Area: {area:.3f}\nCircumference: {circum:.3f}")

main(float(input()))
