"""restaurant"""
def is_food_worth(a, b, c, d):
    """Is the offered food worth?"""
#a = current price, b = promotion price, c = discount%, d = offered food price
    no_offered_discounted = a * ((100-c)/100)
    offered_discounted = (a+d)*((100-c)/100)
    diff_1 = abs(no_offered_discounted-offered_discounted) #a==b
    diff_2 = abs(a-offered_discounted) #a+d >= b
    if a == b: #ถ้าเข้าโปรโมชั่นเลย
        if not d: #offered food เป็น 0 -> ไม่ได้จ่ายเพิ่มจากเดิม
            print("Yes")
        elif no_offered_discounted == offered_discounted: #ไม่ได้จ่ายเพิ่มจากเดิม (ลดมาก็เท่าทุน)
            print("Yes")
        # elif no_offered_discounted > offered_discounted: #สั่งเพิ่มคุ้มกว่า
        #     print(f"Yes {diff_1:.3f}") #อันนี้ไม่ต้องสั่งก็ได้ ยังไง a+d ก็ไม่มีทางคุ้มกว่า d
        else: #offered_discounted > no_offered_discounted สั่งเพิ่มแล้วไม่คุ้ม
            print(f"No {diff_1:.3f}")

    elif a + d >= b: #รับ offer มาแล้วมากกว่าโปรโมชั่น
        if a == offered_discounted:
            print("Yes")
        elif a > offered_discounted:
            print(f"Yes {diff_2:.3f}")
        else: #offered_discounted > a
            print(f"No {diff_2:.3f}")

    else: #ซื้อของแล้วไม่ถึงโปร a + d < b
        print("Yes")
is_food_worth(float(input()), float(input()), float(input()), float(input()))
