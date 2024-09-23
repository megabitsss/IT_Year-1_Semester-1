"""right arrow"""
import math
def main(column, row):
    """main function"""
    upPart = math.ceil(row/2)
    downPart = row//2
    spaces = upPart - 1
    spaces = 0
    for _ in range(1, upPart+1):
        print(" "*spaces, end="")
        print("*"*column)
        spaces += 1
    spaces = downPart-1
    for _ in range(1, downPart+1):
        print(" "*spaces, end="")
        print("*"*column)
        spaces -= 1
main(int(input()), int(input()))
