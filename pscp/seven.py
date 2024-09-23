"""seven"""
def main(num):
    """main function"""
    if num >= 5:
        match num%4:
            case 0:
                print("1")
            case 1:
                print("7")
            case 2:
                print("9")
            case 3:
                print("3")
main(int(input()))
