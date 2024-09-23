"""run length decoding"""
def decoder(message):
    """decode the message from the input"""
    str_num = "" #concatednated num
    for character in message:
        if character.isnumeric():
            str_num += character
        else:
            num = int(str_num)
            print(character * num, end="")
            str_num = "" #reset str_num to default
decoder(input())
