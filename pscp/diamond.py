"""diamond"""   
def diamond_create(size):
    """create a diamond pattern"""
    outerSpace = size // 2
    innerSpace = 0
    for row in range(1, (size//2)+1):
        print(" "*outerSpace, end="")
        print("*", end="")
        print(" "*((innerSpace * 2)-1), end="")
        if row != 1:
            print("*", end="")
        print()
        outerSpace -= 1
        innerSpace += 1
    print("*"*size)
    outerSpace = 1
    innerSpace = (size // 2) - 1
    for row in range(1, (size//2)+1):
        print(" "*outerSpace, end="")
        print("*", end="")
        print(" "*((innerSpace * 2)-1), end="")
        if row != size//2:
            print("*", end="")
        print()
        outerSpace += 1
        innerSpace -= 1
diamond_create(int(input()))

#      *  0
#     * *  1
#    *   *  3
#   *     *  5
#  *       *   7
# **********
#  *
