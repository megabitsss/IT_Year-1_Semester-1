"""Muddled Menu"""
def menu_ordering():
    """Ordering the menu in the properly way"""
    menu_order = []
    while True:
        food = input()
        if food == "DONE":
            break
        if food == "CLOSED":
            menu_order.clear()
            break
        if food == "SOMETHING'S WRONG":
            menu_order.clear()
            continue
        if "Can't do:" in food:
            food_index = food.index(": ")+2
            food = food[food_index:]
            menu_order.remove(food)
        elif "#N" in food:
            last_index = food.index("#")-1
            food = food[:last_index]
            menu_order.append(food)
        else: # #followed with number
            last_index = food.index("#")-1
            index = int(food[food.index("#")+1:]) - 1 #เลขสองหลัก ถ้าslcingไม่ถึงตัวท้ายจะผิด
            food = food[:last_index]
            menu_order.insert(index, food)
    print(f"Full Course: {menu_order} Reversed: {menu_order[::-1]}")
menu_ordering()
