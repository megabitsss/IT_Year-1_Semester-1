"""circular ii"""
import math
def main(circle, they_circle): #x, y, radius are ourselves
    """main func"""
    x, y, radius = circle
    they_x, they_y, they_radius = they_circle
    d = math.sqrt((x-they_x)**2 + (y-they_y)**2) #distance between 2 pts
    sum_radius = radius + they_radius
    if sum_radius > d:
        print("Yes")
    else:
        print("No")
main((float(input()), float(input()), float(input())),\
     (float(input()), float(input()), float(input())))
