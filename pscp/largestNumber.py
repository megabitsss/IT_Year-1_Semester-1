"""largest number"""
def main(num1, num2, num3):
    """main func"""
    if num1 >= num2 and num1 >= num3:
        high = num1
        if num2 >= num3:
            medium, low = num2, num3
        else:
            medium, low = num3, num2

    elif num2 >= num1 and num2 >= num3:
        high = num2
        if num1 >= num3:
            medium, low = num1, num3
        else:
            medium, low = num3, num1

    else:
        high = num3
        if num1 >= num2:
            medium, low = num1, num2
        else:
            medium, low = num2, num1
    print(f"{int(high+medium+low)}")
main(input(), input(), input())
