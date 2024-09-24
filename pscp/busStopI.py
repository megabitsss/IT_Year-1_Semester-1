"""Bus Stop I"""
def bus_catcher(max_bus, point_amount):
    """Catch the people from each bus point"""
    bus_list = []
    current_bus = []
    cnt = 0
    for _ in range(point_amount):
        bus_list.append(input().split())
    bus_list.sort(key=lambda x: int(x[0]))
    for index in range(point_amount):
        number = bus_list[index][0]
        for person in current_bus.copy(): #person leaves the bus
            if person == number: #used .copy() to prevent errors during iteration
                current_bus.remove(person)
                cnt += 1
        for person in bus_list[index][1:]:
            if len(current_bus) < max_bus and int(person) > int(number): #person catches the bus
                current_bus.append(person)
            if len(current_bus) >= max_bus: #if bus is full, end the loop
                break
    print(cnt)
bus_catcher(int(input()), int(input()))
