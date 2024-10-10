"""Pro"""
def pro(come_x, paid_y, buffet_price_a, eat_z):
    """find the buffet promotion"""
    if eat_z >= come_x:
        promotion = eat_z // come_x #หาว่าเข้าโปรกี่ชุด
        paid_amount = eat_z - (promotion * come_x) + (promotion * paid_y)
        #เอาคนที่เหลือไม่ได้เข้าโปร มารวมชุดทั้งหมดว่าเข้าโปรกี่ชุดแล้ว แล้วคูณตามโปร
        price = paid_amount * buffet_price_a
    else:
        price = eat_z * buffet_price_a
    print(price)
pro(int(input()), int(input()), int(input()), int(input()))
