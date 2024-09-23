"""post office"""
def package(item):
    """calculate the weight of package"""
    match item:
        case item if 0 <= item <= 500:
            return 45
        case item if 500 < item <= 1_000:
            return 55
        case item if 1_000 < item <= 2_000:
            return 70
def envelope(item):
    """calculate the weight of envelope"""
    match item:
        case item if 0 <= item <= 10:
            return 16
        case item if 10 < item <= 20:
            return 18
        case item if 20 < item <= 100:
            return 23
        case item if 100 < item <= 250:
            return 28
        case item if 250 < item <= 500:
            return 33
        case item if 500 < item <= 1_000:
            return 48
        case item if 1_000 < item <= 2_000:
            return 68
def item_cal(envelope_amount, package_amount):
    """calculate the price of envelope/package"""
    total = (envelope_amount * 13) + (package_amount * 15)
    for _ in range(envelope_amount):
        item = float(input())
        total += envelope(item)
    for _ in range(package_amount):
        item = float(input())
        total += package(item)
    print(total)
item_cal(int(input()), int(input()))
