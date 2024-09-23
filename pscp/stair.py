"""Stair"""
def stair_step_finder(max_step, stair_n):
    """find the least step you need to step over those stairs"""
    cnt = 1 #ยังไงก็ต้องก้าวแน่ๆ หนึ่งก้าว
    stepped = 0
    No = False
    for _ in range(1, stair_n+1):
        stair = int(input())
        if stair > max_step or not max_step:
            print("NO")
            No = True
            break
        if stepped + stair > max_step:
            stepped = stair #ให้เท่ากับ height stair ขณะนั้น
            cnt += 1
        else:
            stepped += stair
    if not No:
        print(cnt)
stair_step_finder(int(input()), int(input()))
