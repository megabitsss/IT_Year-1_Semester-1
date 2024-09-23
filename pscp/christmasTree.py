"""christmas tree"""
def main(leaf, wood):
    """main func"""
    spacesCnt = leaf - 1
    for i in range(1, leaf+1):
        print(" "*spacesCnt, end="")
        print("*"*(2*i -1))
        spacesCnt -= 1
    middle = leaf
    woodSpaces = middle - 2
    for i in range(1, wood+1):
        print(" "*woodSpaces, end="")
        print("---")
main(int(input()), int(input()))
