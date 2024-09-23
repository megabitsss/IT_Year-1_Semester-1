"""one for all"""
def one_for_all(num):
    """fidning sucessive order"""
    text =""
    for order in range(1, num+1):
        character = input()
        if order == num:
            text += character + "_" + str(order)
        elif not order%2: #Even
            text += character + "-"*order
        elif order%2: #Odd
            text += character + "*"*order
    print(text)
one_for_all(int(input()))
