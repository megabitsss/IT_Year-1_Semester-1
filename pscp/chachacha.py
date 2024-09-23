"""cha cha cha"""
import math
def wage(n):
    """find wage in korean currency"""
    cnt = 0
    for _ in range(n):
        x = math.ceil(float(input()))
        cnt += x
    print(cnt * 8_720)
wage(int(input()))
