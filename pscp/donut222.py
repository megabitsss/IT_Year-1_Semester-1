"""donut without loops"""
def main(a, b, c, d):
    """main func"""
    #a = price
    #b = buy b units to get c units
    #c = get free donuts from promotion
    #d = wanted donut
    freeCnt = d // (b+c) #freeCnt ที่ไม่เกิน d
    freeUnit = freeCnt * (b+c)
    leftDonut = 0
    plusDonut = 0
    if freeUnit < d:
        leftDonut = d - freeUnit
        if leftDonut < b:
            plusDonut = leftDonut
            paidDonut = (freeCnt*b) + leftDonut
        else:
            plusDonut = b + c
            paidDonut = (freeCnt*b) + b
    else:
        paidDonut = freeCnt*b
    sumDonut = freeUnit + plusDonut
    print(f"{paidDonut*a} {sumDonut}")
main(int(input()), int(input()), int(input()), int(input()))
    