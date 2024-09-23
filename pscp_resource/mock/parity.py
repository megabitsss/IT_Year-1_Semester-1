"""parity"""
def bit_1_count(num):
    """#counting 1"""
    cnt = 0
    for i in num:
        match i:
            case "1":
                cnt += 1
    return cnt

def main(num, parity_type):
    """main"""
    bit_1 = bit_1_count(num)
    if not bit_1 % 2: #even
        match parity_type:
            case "Even":
                print(num + "0")
            case "Odd":
                print(num + "1")
    else: #odd
        match parity_type:
            case "Even":
                print(num + "1")
            case "Odd":
                print(num + "0")
main(input(), input())
