"""Tax"""
def cc_cal(cc):
    """calculate car cc"""
    match cc:
        case cc if 1 <= cc <= 600:
            return cc * 0.5
        case cc if 601 <= cc <= 1800:
            return (cc - 600) * 1.5
        case cc if cc >= 1801:
            return (cc - 1800) * 4

def tax(year_used, cc):
    """calculate car tax"""
    match cc:
        case cc if 1 <= cc <= 600:
            cc = cc_cal(cc)
        case cc if 601 <= cc <= 1800:
            cc = cc_cal(cc) + cc_cal(600)
        case cc if cc >= 1801:
            cc = cc_cal(cc) + cc_cal(600) + cc_cal(1800)
    match year_used:
        case 6:
            cc *= 90 / 100
        case 7:
            cc *= 80/100
        case 8:
            cc *= 70/100
        case 9:
            cc *= 60/100
        case year_used if year_used >= 10:
            cc *= 50/100
    print(f"{cc:.2f}")
tax(int(input()), int(input()))
