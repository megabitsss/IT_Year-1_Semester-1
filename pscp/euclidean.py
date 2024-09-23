"""euclidean"""
import math
def main(q1, q2, p1, p2):
    """main func"""
    print(math.sqrt((q1-p1)**2 + (q2-p2)**2))
main(float(input()), float(input()), float(input()), float(input()))
