"""Bus Stop I"""
def bus_catcher(max_bus, point_amount):
    """Catch the people from each bus point"""
    bus_list = []
    cnt = 0
    for _ in range(point_amount):
        new_list = input().split()
        number = new_list[0]
        for person in bus_list.copy(): #person leaves the bus
            if person == number: #used .copy() to prevent errors during iteration
                bus_list.remove(person)
                cnt += 1
        for person in new_list[1:]:
            if len(bus_list) < max_bus and int(person) > int(number): #person catches the bus
                bus_list.append(person)
            if len(bus_list) >= max_bus: #if bus is full, end the loop
                break
    print(cnt)
bus_catcher(int(input()), int(input()))
