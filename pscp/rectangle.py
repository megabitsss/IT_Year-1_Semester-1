"""rectangle"""
def main(h, w):
    """main func"""
    area(h, w)
    perimeter(h, w)
def area(h, w):
    """area func"""
    print(h * w)
def perimeter(h, w):
    """perimeter func"""
    print(2 * h + 2 * w)
main(int(input()), int(input()))
