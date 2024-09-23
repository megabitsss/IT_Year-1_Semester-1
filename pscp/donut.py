"""donut"""
def main(price, promotion, free, wanted):
    """main func"""
    promotion_cnt = 0
    current = 0
    buy = 0
    for _ in range(wanted):
        if current >= wanted: #exits loop when reaches expected donut
            break
        if promotion_cnt >= promotion: #gets free donut
            promotion_cnt = 0
            current += free
        else:
            promotion_cnt += 1
            current += 1
            buy += 1
    print(f"{buy*price} {current}")
main(int(input()), int(input()), int(input()), int(input()), )
