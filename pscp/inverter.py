"""Inverter"""
def inverter_bitwise(binary):
    """change from 1 -> 0, 0 -> 1 and remove all first zero (if it has)"""
    inverted = ""
    for digit in binary:
        if digit == "1":
            inverted += "0"
        else:
            inverted += "1"
    if int(inverted):
        print(int(inverted))
inverter_bitwise(input())
