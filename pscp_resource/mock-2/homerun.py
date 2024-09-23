"""homerun"""
def homerun_finder(n, batter):
    """find homerun score in each field of the player"""
    cnt = 0
    for _ in range(n):
        field_range = float(input())
        if batter > field_range:
            cnt += 1
    print(cnt)
homerun_finder(int(input()), float(input()))
