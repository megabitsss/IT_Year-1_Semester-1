"""number message"""
def number_to_text_replacer(message):
    """replace from number to text"""
    message = message.replace("12", "R") #12 and 13 are the first priority
    message = message.replace("13", "B")
    message = message.replace("1", "I")
    message = message.replace("3", "E")
    message = message.replace("4", "A")
    message = message.replace("5", "S")
    message = message.replace("0", "O")
    for i in "26789": #replace unneccesary number
        message = message.replace(i, "")
    message = message.upper()
    print(message)
number_to_text_replacer(input())
