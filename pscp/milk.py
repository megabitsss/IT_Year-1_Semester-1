"""milk"""
def main(price, promotion, get, money):
    """main func"""
    caps = 0
    received_milk = 0
    if not promotion: #if promotion does not exist
        received_milk = money // price
    else:
        caps += money // price
        received_milk += money // price
        while caps >= promotion:
            caps += get #the caps we get from promotion
            caps -= promotion #the caps we used
            received_milk += get
    print(received_milk)
main(int(input()), int(input()), int(input()), int(input()))
#เอาฝาฟรีมาคิดด้วย ที่ได้จาก promotion
#ฝา = 0
# free = 0 --- old logic
#     buyable = money // price
#     if promotion != 0:
#         free = (buyable // promotion) * get
#         free += (free // promotion) * get
#     sumMilk = free + buyable
#     print(sumMilk)
