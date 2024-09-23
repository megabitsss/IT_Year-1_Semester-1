"""real"""
def binary_maker():
    """create binary number from on/off input"""
    binary = ""
    for _ in range(8): #8 included dp
        digit = input()
        if digit == "on":
            binary += "1"
        else:
            binary += "0"
    return binary
def bin_to_dec(binary):
    """convert binary to decimal number (as a string)"""
    match binary[:7]: #excluded dp
        case "1111110":
            result = "0"
        case "0110000":
            result = "1"
        case "1101101":
            result = "2"
        case "1111001":
            result = "3"
        case "0110011":
            result = "4"
        case "1011011":
            result = "5"
        case "1011111":
            result = "6"
        case "1110000":
            result = "7"
        case "1111111":
            result = "8"
        case "1111011":
            result = "9"
        case _: #wrong binary pattern
            result = "Error"
    return result
def dp(binary):
    """check for decimal point"""
    match binary[-1]:
        case "1":
            return "."
        case "0":
            return ""
def main():
    """main process of checking if the binary is legit"""
    concat_num = ""
    for _ in range(3):
        binary = binary_maker()
        concat_num += bin_to_dec(binary) + dp(binary)
    if concat_num.count(".") > 1 or "Error" in concat_num:
        print("Error")
    else:
        print(f"{float(concat_num):.2f}")
main()
