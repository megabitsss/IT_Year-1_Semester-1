"""circular i"""
import math
def main(human_x, human_y, radius, mosq_x, mosq_y): #mosq = mosquito
    """main func"""
    d = math.sqrt((human_x-mosq_x)**2 + (human_y-mosq_y)**2) #distance between 2 points
    if d <= radius:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
