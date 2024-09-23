"""shorten"""
def shortener():
    """shorten the number"""
    num = int(input())
    start = num
    stop = num
    result = ""
    while num != -1:
        num = int(input())
        if num == -1: #มาเช็คครั้งสุดท้ายอีกรอบนึงว่าเลขเป็นยังไง start, stop
            if abs(start-stop) >= 1: #more than one number
                result += str(start) + "-" + str(stop)
            else: #only one number
                result += str(stop)
            start = stop = num
            break
        if abs(num-stop) == 1:
            stop = num
        else:
            if abs(start-stop) >= 1: #more than one number
                result += str(start) + "-" + str(stop) + ", "
            else: #only one number
                result += str(stop) + ", "
            start = stop = num
    print(result)
shortener()
# 12
# 15
# 16
# 17
# 19
# -1

# 12
# 15
# 16
# 17
# 18
# -1
