"""distribute"""
def money_distributor(money, child):
    """calculate the money in the family, liking 8Baht, not liking 4Baht"""
    eight_cnt = 0
    sigma = 0
    child_cnt = 0
    for _ in range(child):
        if sigma + 8 <= money:
            sigma += 8
            eight_cnt += 1
            child_cnt += 1
        else: #more than money
            diff = money - sigma
            sigma += diff
            child_cnt += 1
            if child_cnt < child:
                while child_cnt < child:
                    diff -= 1
            if diff == 4:
                eight_cnt -= 1
    print(eight_cnt)
money_distributor(int(input()), int(input()))
