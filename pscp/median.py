"""Median"""
import math
def median_finder(n):
    """Find the median value"""
    my_list = []
    for _ in range(n):
        my_list.append(float(input()))
    my_list.sort()
    pos = ((n+1)/2)-1
    if not n%2: #even
        first_pos = int(pos)
        second_pos = math.ceil(pos)
        pos = (my_list[first_pos]+my_list[second_pos])/2
    else: #odd
        pos = my_list[int(pos)]
    print(f"{pos:.3f}")
median_finder(int(input()))
