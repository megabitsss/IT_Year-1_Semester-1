"""Point Sorting"""
def fx(point_list):
    """function that returns x+y and greater y is prioritized"""
    x = int(point_list[0])
    y = int(point_list[1])
    return x+y, -y


def point_sorter(dataset):
    """sort the point by x+y and if y is equal, greater y will be prioritized"""
    sublist = []
    for _ in range(dataset):
        subdataset = int(input())
        for _ in range(subdataset):
            point = input()
            sublist.append(point.split())
        sublist.sort(key=fx)
        for each_list in sublist:
            print(" ".join(each_list))
        sublist.clear()
point_sorter(int(input()))
