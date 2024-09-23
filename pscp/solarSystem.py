"""Solar System"""

def planet(orbit):
    """Find the hottest and the coolest planet"""
    def sun_index_finder(orbit):
        """Find the index of Sun that is not 'Suns', 'Sunz', etc."""
        leftmost_spc = orbit.find(" ")
        rightmost_spc = orbit.rfind(" ")
        if orbit[:leftmost_spc] == "Sun":
            return 0
        elif orbit[rightmost_spc+1:] == "Sun":
            return -3
        else:
            index_swap = 0
            while True:
                first_spc = orbit.find(" ", index_swap)
                second_spc = orbit.find(" ", first_spc+1)
                if orbit[first_spc+1:second_spc] == "Sun":
                    return first_spc + 1
                else:
                    index_swap = second_spc
    def one_planet(orbit):
        """one planet in solar system ex. Sun Mars"""
        if orbit.count(" ") == 1:
            return True
        return False
    def sun_mid(orbit):
        """sun is at the middle and 2 planets"""
        if orbit.count(" ") == 2 and orbit[leftmost_1st+1:rightmost_1st] == "Sun":
            return True
        return False
    def primary(orbit):
        """Sun is the leftest/righest""" #Sun อยู่ริมสุดซ้าย/ขวา
        if "Sun" in (orbit[:leftmost_1st], orbit[rightmost_1st+1:]):
            return True
        return False
    def secondary(orbit):
        """Sun is at after the first/before the end""" #Sun อยู่หลังแรกสุด/ก่อนท้ายสุด
        sun_first = orbit[leftmost_1st+1:leftmost_2nd]
        sun_last = orbit[rightmost_2nd+1:rightmost_1st]
        if "Sun" in (sun_first, sun_last):
            return True
        return False
    leftmost_1st = orbit.find(" ") #leftest space index
    rightmost_1st = orbit.rfind(" ") #rightest space index
    leftmost_2nd = orbit.find(" ", leftmost_1st+1)
    rightmost_2nd = orbit.rfind(" ", 0, rightmost_1st-1)
    leftmost_3rd = orbit.find(" ", leftmost_2nd+1)
    rightmost_3rd = orbit.rfind(" ", 0, rightmost_2nd-1)
    sun_index = sun_index_finder(orbit)
    sun_leftmost_1st = sun_index - 1 #Sun left space
    sun_rightmost_1st = sun_index + 3 #Sun right space
    sun_leftmost_2nd = orbit.rfind(" ", 0, sun_leftmost_1st)
    sun_rightmost_2nd = orbit.find(" ", sun_rightmost_1st+1)
    if one_planet(orbit):
        if "Sun" == orbit[:3]: #Leftset
            print(f"Hot: {orbit[leftmost_1st+1:]}")
            print(f"Cool: {orbit[leftmost_1st+1:]}")
        else: #Rightest
            print(f"Hot: {orbit[:leftmost_1st]}")
            print(f"Cool: {orbit[:leftmost_1st]}")
    elif sun_mid(orbit):
        print(f"Hot: {orbit[:leftmost_1st]} {orbit[rightmost_1st+1:]}")
        print(f"Cool: {orbit[:leftmost_1st]} {orbit[rightmost_1st+1:]}")
    elif primary(orbit): #Primary***
        if "Sun" == orbit[:leftmost_1st]: #Leftest
            print(f"Hot: {orbit[leftmost_1st+1:leftmost_2nd]}")
            print(f"Cool: {orbit[rightmost_1st+1:]}")
        else: #Rightest
            print(f"Hot: {orbit[rightmost_2nd+1:rightmost_1st]}")
            print(f"Cool: {orbit[:leftmost_1st]}")
    elif secondary(orbit): #Second***
        if "Sun" == orbit[leftmost_1st+1:leftmost_2nd]: #Leftest
            print(f"Hot: {orbit[:leftmost_1st]} {orbit[leftmost_2nd+1:leftmost_3rd]}")
            print(f"Cool: {orbit[rightmost_1st+1:]}")
        else: #Rightest
            print(f"Hot: {orbit[rightmost_3rd+1:rightmost_2nd]} {orbit[rightmost_1st+1:]}")
            print(f"Cool: {orbit[:leftmost_1st]}")
    else: #Sun is at the center; คือ Sun ไม่ได้เป็น Primary/Secondary
        left_cnt = orbit[:sun_leftmost_1st+1].count(" ")
        right_cnt = orbit[sun_rightmost_1st:].count(" ")
        print(f"Hot: {orbit[sun_leftmost_2nd+1:sun_leftmost_1st]} {orbit[sun_rightmost_1st+1:sun_rightmost_2nd]}")
        if left_cnt < right_cnt:
            print(f"Cool: {orbit[rightmost_1st+1:]}")
        elif left_cnt > right_cnt:
            print(f"Cool: {orbit[:leftmost_1st]}")
        else: #left_cnt == right_cnt
            print(f"Cool: {orbit[:leftmost_1st]} {orbit[rightmost_1st+1:]}")
planet(input())


# This Problem Keys
# - you can use orbit.find(" Sun ") for preventing weird sun names
# - you can use " " + orbit " " to prevent the issues that might occur from previous number
# - enumerate is also good
# - String Slicing ถ้ามันเกินก็สามารถทำให้รวมโค้ดในที่เดียวกันได้