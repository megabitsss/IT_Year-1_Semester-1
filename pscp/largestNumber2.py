"""largest number"""
def main(x, y, z):
    """main function"""
    num1 = x + y + z
    num2 = x + z + y
    num3 = y + x + z
    num4 = y + z + x
    num5 = z + x + y
    num6 = z + y + x
    # num1 = int(num1)
    # num2 = int(num2)
    # num3 = int(num3)
    # num4 = int(num4)
    # num5 = int(num5)
    # num6 = int(num6)
    highest = num1
    if num2 > highest:
        highest = num2
    if num3 > highest:
        highest = num3
    if num4 > highest:
        highest = num4
    if num5 > highest:
        highest = num5
    if num6 > highest:
        highest = num6
    print(int(highest))
main(input(), input(), input())
