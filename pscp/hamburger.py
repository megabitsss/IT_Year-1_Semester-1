"""hamburger"""
def main():
    """main func"""
    left_bread = int(input())
    right_bread = int(input())
    print("|"*left_bread + "*"*left_bread*2\
            + "*"*right_bread*2 + "|"*right_bread)
main()
