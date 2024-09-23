"""coffee shop"""
def coffee_promotion_checker(a, b, c, d, e):
    """checking whether promotion 1 or promotion 2 is more worth"""
    #coffee [a] price, buy amount of [e]
    #promotion_1 = fisrt cup [a], the left each got discounted [b]%
    #promotion_2 = [c]% discouted if minimum is [d] baht
    promotion_1 = a + (e-1)*(a*((100-b)/100))
    promotion_2 = a * e
    if promotion_2 >= d: #if greater than minimum
        promotion_2 *= ((100-c)/100)
    if promotion_2 <= promotion_1:
        print(f"2\n{promotion_2:.2f}")
    else:
        print(f"1\n{promotion_1:.2f}")
coffee_promotion_checker(float(input()), float(input()), float(input()),\
                        float(input()), int(input()))
