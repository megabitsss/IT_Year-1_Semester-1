"""Ascending Sort"""
def sorter(n):
    """sorting the list"""
    my_list = []
    for _ in range(n):
        my_list.append(int(input()))
    my_list.sort()
    for item in my_list:
        print(item)
sorter(int(input()))
