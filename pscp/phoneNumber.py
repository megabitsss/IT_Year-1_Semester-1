"""Phone Number"""
def phone_checker(number, country):
    """phone number checker"""
    match country:
        case "Domestic":
            match len(number):
                case 10:
                    phone = number[:2] + " " + number[2:6] + " " + number[6:]
                case 9:
                    phone = number[:1] + " " + number[1:5] + " " + number[5:]
        case "International":
            match len(number):
                case 10:
                    phone = "+66" + number[1] + " " + number[2:6] + " " + number[6:]
                case 9:
                    phone = "+66 " + number[1:5] + " " + number[5:]
    print(phone)
phone_checker(input(), input())
