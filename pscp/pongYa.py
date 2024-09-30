"""PongYa"""
def pong_ya(number):
    """PongYa Calculator"""
    if not int(number) % 3 or number[-1] == "3":
        print("PONG")
    else:
        print(number)
pong_ya(input())
