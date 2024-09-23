"""run length encoding"""
def letter_printing(message):
    """print encoded letter"""
    print(message.count(message[0]), message[0], sep="", end="")
    #even message[0] it's still this form 'aaa','bb',etc.
def encoder(message):
    """encoder the code from the input"""
    len_message = len(message)
    message = message + " " #adding due to message[index] != message[index+1] runs out of index
    start = 0
    stop = 0
    for index in range(0, len_message):
        if message[index] != message[index+1]:
            stop = index + 1
            letter_printing(message[start:stop])
            start = index + 1
encoder(input())
