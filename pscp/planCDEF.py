"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main(order, x1, x2, x3):
    """main func"""
    if x1 >= x2 >= x3:
        high = x1
        if x2 >= x3:
            medium = x2
            low = x3
        else:
            medium = x3
            low = x2
    elif x2 >= x1 >= x3:
        high = x2
        if x1 >= x3:
            medium = x1
            low = x3
        else:
            medium = x3
            low = x1
    else:
        high = x3
        if x1 >= x2:
            medium = x1
            low = x2
        else:
            medium = x2
            low = x1
    if order == "Ascend":
        print(f"{low:.2f}, {medium:.2f}, {high:.2f}")
    else:
        print(f"{high:.2f}, {medium:.2f}, {low:.2f}")
main(input(), float(input()), float(input()), float(input()))
