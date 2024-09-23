"""it business"""
def money_finder(money_bank, money_wallet):
    """runs the program if input is Deposit or Withdraw"""
    error = 0
    while True:
        state = input()
        if state == "end":
            break
        money = float(state[2:])
        match state[0]:
            case "D": #deposit wallet -> bank
                if money_wallet >= money:
                    money_wallet -= money
                    money_bank += money
                    error = 0
                else:
                    error += 1
            case "W": #withdraw bank -> wallet
                if money_bank >= money:
                    money_wallet += money
                    money_bank -= money
                    error = 0
                else:
                    error += 1
        if error >= 3: #keyword is error ติดกันครั้ง
            break
    print(f"{money_bank:.2f}")
    print(f"{money_wallet:.2f}")
money_finder(float(input()), float(input()))
