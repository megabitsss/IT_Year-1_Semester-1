"""weight station"""
def main(avg, wheel1, wheel2, wheel3):
    """main func"""
    wheel4 = (avg*4)-wheel1-wheel2-wheel3
    wheelSum = wheel1 + wheel2 + wheel3 + wheel4
    halfAvg = avg/2
    if wheelSum > 15000 and (abs(wheel1-avg)>halfAvg or abs(wheel2-avg)>halfAvg\
                              or abs(wheel3-avg)>halfAvg or abs(wheel4-avg)>halfAvg):
        print("Overweight")
    else:
        if wheelSum > 15000:
            print("Overweight")
        elif abs(wheel1-avg)>halfAvg or abs(wheel2-avg)>halfAvg or\
            abs(wheel3-avg)>halfAvg or abs(wheel4-avg)>halfAvg:
            print("Unbalance")
        else:
            print(f"Pass {wheel4:.2f}")
main(float(input()), float(input()), float(input()), float(input()))
