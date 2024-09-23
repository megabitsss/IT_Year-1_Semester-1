"""coke"""
def main(normal_price, promotion, special_price, wanted):
    """coke"""
    normal_amount = 0
    special_amount = 0
    total_amount = 0
    for _ in range(wanted):
        total_amount += 1
        if promotion: #if promotion != 0
            if total_amount > promotion: #???
                special_amount += 1
                total_amount = 1
            else:
                normal_amount += 1
        else:
            normal_amount = wanted
            break
    total = (normal_amount * normal_price) + (special_amount * special_price)
    print(total)
main(int(input()), int(input()), int(input()), int(input()))
