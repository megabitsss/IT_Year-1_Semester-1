"""CoinChange V1"""
def coin_cnt(n):
    """count the least posible coin(s)"""
    cnt = 0
    for i in (25, 10, 5, 1):
        cnt += n // i
        n -= (n // i) * i
    print(cnt)
coin_cnt(int(input()))
