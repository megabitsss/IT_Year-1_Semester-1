"""bad keyboard"""
def keyboard_debugger(txt):
    """switch between i, o, I, O"""
    empty_str = ""
    for char in txt:
        if char == "i":
            empty_str += "o"
        elif char == "o":
            empty_str += "i"
        elif char == "I":
            empty_str += "O"
        elif char == "O":
            empty_str += "I"
        else:
            empty_str += char
    print(empty_str)
keyboard_debugger(input())
