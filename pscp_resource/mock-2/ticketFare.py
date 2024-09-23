"""ticket fare"""
def fare_cal():
    """calculate the fare of ticket"""
    N = int(input()) #termination
    a = int(input()) #level 1 threshold
    b = int(input()) #level 1 adding
    c = int(input()) #level 2 threshold
    d = int(input()) #level 2 adding
    e = int(input()) #level 3 adding
    f = int(input()) #start
    g = int(input()) #stop
    b_point = a + b
    money = 0
    station_amount = 0
    station_most = abs(f-g) #termination
    station_amount += a
    money += b
    if station_amount < a: #a ended
        return money
    else:
        station_amount = a #ถ้าเกิน set กลับไว้ที่ a
    if station_amount + c < b_point: #บวกแล้วไม่เกิน
        money += d * abs(station_amount-g)
        return money
    else: #level 2 กรณีเท่ากับหรือเกิน
        station_amount = c
        money += abs(b_point - a) * e
print(fare_cal())
