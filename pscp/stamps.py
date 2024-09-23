"""Stamps"""
import math
def stamp_cal():
    """Calculate the rest stamps and paid bill after discounted"""
    food_amount = int(input()) #n
    food_promotion = int(input()) #a
    stamp_get = int(input()) #b
    stamp_promotion = int(input()) #c
    discount = int(input()) #d
    stamp_current = 0
    paid = 0
    for _ in range(food_amount):
        food = int(input())
        discount_money = 0
        if stamp_current >= stamp_promotion:
            max_discount = (stamp_current//stamp_promotion) * discount
            if food >= max_discount: #ใช้ให้หมด!
                stamp_used = (stamp_current // stamp_promotion) * stamp_promotion
            #ใช้ // เพราะบางหารแล้วมีเศษเหลือ เราไม่จำเป็นต้องใช้ให้หมด เช่น มี 11 ดวง แต่ใช้ทุก ๆ 2 ดวง
            else: #food < max_discount
                stamp_used = math.ceil(food/discount) * stamp_promotion
            discount_money += (stamp_used//stamp_promotion) * discount
            stamp_current -= stamp_used
        food = max(0, food - discount_money) #ลดราคาอาหาร
        if food >= food_promotion:
            stamp_current += (food // food_promotion) * stamp_get
        paid += food
    print(paid)
    print(stamp_current)
stamp_cal()
