"""calculator"""
def cal(n):
    """main"""
    num_str = ""
    for num in range(1,n+1): #กดเลขอย่างเดียว อาจจะมีกรณีกดเลขหลักที่ >= 2
        num_str += str(num)
    match n:
        case 1:
            print("1")
        case _:
            print(len(num_str) + n)
cal(int(input()))
