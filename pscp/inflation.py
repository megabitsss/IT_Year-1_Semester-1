"""Inflation"""
def inflationer():
    """find the inflated money"""
    money = int(float(input()) * 100) #added 2 digits
    year = int(input())
    rate = 381 #3.81 * 100 (added 2 digits)
    for _ in range(year):
        money += (money * rate) // 10_000
    print(f"{money//100}.{money%100:02d}")
inflationer()
#100, 2 -> 107.76
#10_000 + 381 = 10_381
#10_381 + 395 = 10_776
