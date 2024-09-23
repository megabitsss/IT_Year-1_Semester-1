"""Sequence XXX"""
import math
def top_left(size, amount):
    """create top/left row"""
    for _ in range(amount):
        print("*"*size, end=" ")
def rectangle_maker(size, amount):
    """createn a diagonal rectangle"""
    empty_row = ""
    diagonal = size - 2 #minus top and left as (-2)
    foward = 1
    backward = size
    diag_first = math.ceil(diagonal / 2)
    top_left(size, amount)
    print()
    for n in range(1, diagonal+1):
        empty_row = ""
        if n <= diag_first:
            foward += 1
            backward -= 1
        else: #diag_last = diagonal//2
            foward -= 1
            backward += 1
        for index in range(1, size+1): #horizontal
            if index in (1, size, foward, backward):
                empty_row += "*"
            else:
                empty_row += " "
        for _ in range(amount):
            print(empty_row, end=" ")
        print()
    if not size == 1:
        top_left(size, amount)
rectangle_maker(int(input()), int(input()))
