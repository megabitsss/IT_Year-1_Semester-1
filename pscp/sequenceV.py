"""sequence v"""
def main(n):
    """main func"""
    cnt = 0
    for i in range(n, 0, -1):
        print(i, end=" ")
        cnt += 1
        if cnt >= 7:
            print()
            cnt = 0
main(int(input()))
