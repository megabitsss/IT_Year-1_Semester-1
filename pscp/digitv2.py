"""Digitv2"""
def digit_finder(txt):
    """convert from text to number and return its digit"""
    two_digit = ("ten", "eleven", "twelve", "teen", "ty")
    if "thousand" in txt:
        print(4)
    elif "hundred" in txt:
        print(3)
    elif any(x in txt for x in two_digit):
        print(2)
    else:
        print(1)
    print([x + " Hello" for x in two_digit])
digit_finder(input())
