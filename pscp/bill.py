"""bill"""
def main(price):
    """main func"""
    if 0.1 * price < 50:
        service = 50
    elif 0.1 * price > 1_000:
        service = 1_000
    else:
        service = price * 0.1
    vat = (service + price) * 0.07
    print(f"{price + vat + service:.2f}")
main(int(input()))
