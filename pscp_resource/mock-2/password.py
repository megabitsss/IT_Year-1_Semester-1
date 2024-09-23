"""password"""
import math
def char_type_checker(char):
    """returns type a char -> lower, upper, numeric, printalbe"""
    if char.isupper():
        return "Upper"
    if char.islower():
        return "Lower"
    if char.isnumeric():
        return "Numeric"
    return "Printable"
def password_entropy_finder(password):
    """returns password entropy and its strengthness"""
    uppercase = True
    lowercase = True
    numeric = True
    printalble = True
    R = 0 #Pool size
    L = len(password) #Password length
    for char in password:
        char_type = char_type_checker(char)
        if uppercase and char_type == "Upper":
            R += 26
            uppercase = False
        elif lowercase and char_type == "Lower":
            R += 26
            lowercase = False
        elif numeric and char_type == "Numeric":
            R += 10
            numeric = False
        elif printalble and char_type == "Printable":
            R += 32
            printalble = False
    entropy = math.floor(math.log(R**L, 2))
    print(entropy)
    match entropy:
        case entropy if entropy < 28:
            print("Very Weak")
        case entropy if 28 <= entropy <= 35:
            print("Weak")
        case entropy if 36 <= entropy <= 59:
            print("Reasonable")
        case entropy if 60 <= entropy <= 127:
            print("Strong")
        case entropy if entropy >= 128:
            print("Very Strong")
password_entropy_finder(input())
