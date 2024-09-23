"""sequence ix"""
def main(n):
    """main func"""
    spaces = "   "
    spaceCnt = n-1
    for i in range(1, n+1):
        print(spaces*spaceCnt, end="")
        spaceCnt -= 1
        for j in range(1, i+1):
            print(f"{j:02}", end=" ")
        for j in range(i-1, 0, -1):
            print(f"{j:02}", end=" ")
        print()
main(int(input()))
     