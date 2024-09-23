"""sequence iv"""
def main(n):
    """main func"""
    start = 1
    stop = n
    for _ in range(1, n+1):
        for j in range(start, stop+1):
            print(j, end=" ")
        print()
        start += n
        stop += n
main(int(input()))
