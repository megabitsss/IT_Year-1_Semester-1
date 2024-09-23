"""sequence viii"""
def main(n):
    """main func"""
    spaceStart = n-1
    for i in range(1, n+1):
        print("   "*spaceStart, end="")
        spaceStart -= 1
        for j in range(1, i+1):
            print(f"{j:02}", end=" ")
        print()
main(int(input()))
