"""coke"""
def coke(normal_price, promotion, special_price, wanted):
    """finding how much money we need to pay for d bottle(s)"""
    #find the amount of special bottles
    special_amount = wanted // promotion
    normal_amount = wanted - special_amount
    