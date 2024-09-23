"""Line Sorting"""
def len_sort(n):
    """Sort list by its element length"""
    my_list = []
    for _ in range(n):
        my_list.append(input())
    my_list.sort(key=len)
    for item in my_list:
        print(item)
len_sort(int(input()))
