"""sequence iii"""
def main(n):
    """main func"""
    start = 2
    stop = n+2
    for _ in range(1, n+1):
        for j in range(start, stop):
            print(j, end=" ")
        print()
        start += 1
        stop += 1
main(int(input()))
