"""Seeker"""
def sum_decoder(txt):
    """Get the sum from encoded message"""
    num = ""
    my_list = []
    for char in txt:
        if char.isdigit():
            num += char
        else:
            my_list.append(num)
            num=""
    print(my_list)
sum_decoder(input())
