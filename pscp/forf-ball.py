"""for!f-ball"""
def decoder(character, pos):
    if character == "A" and pos != 3:
        return "2"
    elif character == "B" and pos != 1:
        return ""

def ball_swap(code):
    """process of swaping balls"""
    position = "100" #means that 1 0 0
    for character in code:
        position = decoder(character, position)
    print(position.find("1") + 1) #plus 1 due to index starts at zero
ball_swap(input())
