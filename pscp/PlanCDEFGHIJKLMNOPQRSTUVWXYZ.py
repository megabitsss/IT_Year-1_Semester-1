"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main(order, num1, num2, num3):
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

    if order == "Ascend":
        print(f"{low:.2f}, {medium:.2f}, {high:.2f}")
    else:
        print(f"{high:.2f}, {medium:.2f}, {low:.2f}")
main(input(), float(input()), float(input()), float(input()))
