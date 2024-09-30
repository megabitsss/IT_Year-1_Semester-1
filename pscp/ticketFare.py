"""Ticket Fare"""
def ticket_cal():
    """Calculate user's ticket price"""
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    traveled = 0
    money = 0
    will_travel = abs(f-g)
    money += b
    traveled += a
    if will_travel > a: #ที่ต้องไปทั้งหมด มากกว่า a ไหม
        #หาต่อว่า class_2nd มีอีกกี่สถานี
        class_2nd = a + c
        if will_travel > class_2nd: #ที่จะไปมากกว่า class 2 ไหม
            #ที่เหลือก็มาหักลบกับ e ไปเลย
            money += (class_2nd - traveled) * d
            traveled += c
            money += (will_travel-traveled) * e
        else:
            money += (will_travel - traveled) * d
    if f > n or g > n:
        print("Error")
    else:
        print(money)
ticket_cal()
