"""sequence N"""
def main(n):
    """main func"""
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j in (1, n, i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
