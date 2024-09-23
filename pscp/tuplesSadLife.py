"""Tuple's Sad Life"""
def tuple_maker(string, target):
    """tuple methods"""
    my_tuple  = string.split()
    my_tuple = tuple(my_tuple)
    first_index = my_tuple.index(target)
    count_target = my_tuple.count(target)
    for _ in range(count_target):
        for _ in range(count_target):
            print(first_index, end=" ")
        print()
tuple_maker(input(), input())
