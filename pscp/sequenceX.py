"""sequence x"""
def main(n):
    """main func"""
    spaces = "   "
    spacesCnt = n-1
    #first half
    for i in range(1, n+1):
        print(spaces*spacesCnt, end="") #spaces
        spacesCnt -= 1
        for j in range(1, i+1): #ascend
            print(f"{j:02}", end=" ")
        for j in range(i-1, 0, -1): #descend
            print(f"{j:02}", end=" ")
        print()

    #second half
    spacesCnt = 1
    stop = n
    for _ in range(1, n):
        print(spaces*spacesCnt, end="") #spaces
        spacesCnt += 1
        for j in range(1, stop):
            print(f"{j:02}", end=" ")
        for j in range(stop-2, 0, -1):
            print(f"{j:02}", end=" ")
        print()
        stop -= 1
main(int(input()))
