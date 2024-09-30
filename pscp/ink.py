"""ink"""
import math
def ink():
    """ink rate"""
    rate_area, n = map(float, input().split())
    for _ in range(1, int(n)+1):
        x, y = map(float, input().split())
        if not x and not y:
            print(0)
            continue
        time = (3.1416/rate_area)*(x**2 + y**2)
        print(math.ceil(time))
ink()
