"""Seeker"""
def sum_decoder(txt):
    """Get the sum from encoded message"""
    txt += " "
    num = ""
    total = 0
    for char in txt:
        if char.isnumeric():
            num += char
        else:
            if not num:
                continue
            total += int(num)
            num = ""
    print(total)
sum_decoder(input())
