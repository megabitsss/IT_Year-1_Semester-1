"""encoding"""
def encoder(message):
    """encode the message"""
    message += " "
    sigma = 0
    pivot = message[0] #the first letter of each group
    for letter in message:
        if letter == pivot:
            sigma += 1
        else:
            print(sigma, pivot, sep="", end="")
            pivot = letter #set new pivot
            sigma = 1 #set new sum, included the current one, so its 1
encoder(input())
