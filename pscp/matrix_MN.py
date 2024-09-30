"""Matrinx_MN"""
def matrix_maker(row, column):
    """make a matrix in m x n form"""
    for _ in range(row):
        row_matrix = ""
        for _ in range(column):
            row_matrix += input() + " "
        print(row_matrix)
matrix_maker(int(input()), int(input()))
