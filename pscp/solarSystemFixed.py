"""Solar System"""
def main(orbit):
    """Finding the hottest and coolest planets"""
    orbit = " " + orbit + " "
    coolest = ""
    hottest = ""
    sun_index = orbit.find(" Sun ")#Starts at 'S'
    left_spaces = 0
    right_spaces = 0
    for index, letter in enumerate(orbit):
        if index in (0, len(orbit)-1): #ถ้าindexเป็นตัวแรกหรือตัวท้ายให้ข้ามไปเลย เพราะมันเป็นspace
            continue
        if index <= sun_index and letter == " ":
            left_spaces += 1
        elif index > sun_index and letter == " ":
            right_spaces += 1
    if left_spaces > right_spaces: #left_spaces is the coolest
        coolest += orbit[1:orbit.find(" ", 1)] #เริ่มจาก 1 ไม่เอา space ตัวแรก
    elif right_spaces > left_spaces:
        coolest += orbit[orbit.rfind(" ", 0, -2)+1:-1]
    else: #left_spaces = right_spaces
        coolest += orbit[1:orbit.find(" ", 1)] + " " + orbit[orbit.rfind(" ", 0, -2)+1:-1]
    #checking for hot
    if sun_index: #ถ้า sun_index == 0 ก็คือซ้ายสุด
        #sun's left planet
        space = orbit.rfind(" ", 0, sun_index) #หา space ก่อนถึง sun_index
        hottest += orbit[space+1:sun_index] + " "
    space = orbit.find(" ", sun_index+5)
    hottest += orbit[sun_index+5:space] #find the rightest hottest, ถ้ามันไม่มีเดี๋ยว slicingไม่เจอ
    print(f"Hot: {hottest}")
    print(f"Cool: {coolest}")
main(input())
