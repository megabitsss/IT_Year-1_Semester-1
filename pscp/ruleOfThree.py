"""rule of three"""
def main(size):
    """main function"""
    bestPerUnit = 0 #grams / price (per 1 price unit)
    bestGrams = 0
    bestPrice = 0
    for _ in range(1, size+1):
        price = float(input())
        grams = float(input())
        if grams / price > bestPerUnit:
            bestPrice = price
            bestGrams = grams
            bestPerUnit = grams / price
        if grams / price == bestPerUnit:
            if min(price, bestPrice) == price:
                bestPrice, bestGrams = price, grams
    print(f"{bestPrice:.2f} {bestGrams:.2f}")
main(int(input()))
