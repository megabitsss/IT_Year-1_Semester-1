"""it business"""
def text_and_num(state):
    """split between text and number"""
    number = ""
    text = ""
    for letter in state:
        if letter.isnumeric():
            number += letter
        elif letter.isalpha():
            text += letter
    return text, float(number)
def money_finder(money_bank, money_wallet):
    """runs the program if input is Deposit or Withdraw"""
    error = 0 #keyword is ติดต่อกัน
    while True:
        state = input()
        if state == "end" or (error >= 3):
            break
        text, money = text_and_num(state)
        # money = float(state[2:])
        match text:
            case "D":
                if money_wallet >= money:
                    money_wallet -= money
                    money_bank += money
                    error = 0
                else:
                    error += 1
            case "W":
                if money_bank >= money:
                    money_wallet += money
                    money_bank -= money
                    error = 0
                else:
                    error += 1
    print(f"{money_bank:.2f}")
    print(f"{money_wallet:.2f}")
money_finder(float(input()), float(input()))
