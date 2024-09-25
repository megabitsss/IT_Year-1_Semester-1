"""ink"""
def ink():
    """ink rate"""
    rate_area, n = input().split()
    for number in range(1, n+1):
        radius = (rate_area/3.1416)**0.5
        coordinate = input().split()
        x,y = coordinate
        if not x and not y: #หยดปุ๊ปจบเลย
            print(0)
            continue
        distance = (x**2 + y**2)**0.5

        

def main():
    """find each houses time"""

ink()
