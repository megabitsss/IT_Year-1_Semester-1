"""Volleyball"""
def main(matches):
    """volleyball"""
    a = 0
    b = 0 #best of three score
    a_pts = 0
    b_pts = 0 #each round score
    set_num = 1
    win_needed = 25
    for point in matches:
        if point == "A":
            a_pts += 1
        else: # "B"
            b_pts += 1
        if a_pts > b_pts and a_pts >= win_needed and abs(a_pts-b_pts) >= 2:
            print(f"Set {set_num}: A ({a_pts}) | B ({b_pts})")
            a += 1
            a_pts = b_pts = 0
            set_num += 1
        elif b_pts > a_pts and b_pts >= win_needed and abs(a_pts-b_pts) >= 2: #b wons set 1 to 4
            print(f"Set {set_num}: A ({a_pts}) | B ({b_pts})")
            b += 1
            a_pts = b_pts = 0
            set_num += 1
        if set_num >= 5:
            win_needed = 15
    if a < 3 and b < 3: #Game has not finished, both are less than 3
        print(f"Set {set_num}: A ({a_pts}) | B ({b_pts})") #Print กรณีล่าสุดเอาไว้ตลอด ถ้าไม่ชนะ
        print("The game has not finished yet.")
    else: #Either A or B wins
        if a > b:
            print(f"A won {a}:{b} set")
        else:
            print(f"B won {b}:{a} set")
main(input())
