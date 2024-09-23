"""Align"""
def centerer(txt, size):
    """center the text"""
    leftSpace = size - len(txt)
    remainedLeft = leftSpace//2 + (leftSpace%2) #leftSpace%2 -> ถ้าเป็นคี่ + 1 และคู่ไม่ต้องบวก
    remainedRight = leftSpace//2
    return (" "*remainedLeft) + txt + (" "*remainedRight)

def main() :
    """aligning program"""
    size = int(input())
    align = input()
    txt = input()
    txtlen = len(txt)
    spaces = size - txtlen
    if align == "left":
        print(txt + " " *spaces)
    elif align == "right":
        print((" " * spaces) + txt)
    elif align == "center":
        print(centerer(txt, size))
main()
