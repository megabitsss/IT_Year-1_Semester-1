"""indicator"""
def main(k, n):
    """main func"""
    for i in range(n//2,0,-1):
        print(" "*i + "*"*k)
    print("*"*k)
    for i in range(1,(n//2)+1):
        print(" "*i + "*"*k)

main(int(input()), int(input()))
