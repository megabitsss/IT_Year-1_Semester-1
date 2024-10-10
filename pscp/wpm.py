"""WPM"""
def wpm(category, speed):
    """find whether you are kid/adult and return wpm levels"""
    match category:
        case "Kids":
            match speed:
                case speed if speed < 11:
                    print("Very Slow")
                case speed if 11 <= speed <= 20:
                    print("Slow")
                case speed if 21 <= speed <= 30:
                    print("Average")
                case speed if 31 <= speed <= 40:
                    print("Fast")
                case _:
                    print("Very Fast")
        case "Adults":
            match speed:
                case speed if speed < 26:
                    print("Very Slow")
                case speed if 26 <= speed <= 35:
                    print("Slow/Beginner")
                case speed if 36 <= speed <= 45:
                    print("Intermediate/Average")
                case speed if 46 <= speed <= 65:
                    print("Fast/Advanced")
                case speed if 66 <= speed <= 80:
                    print("Very Fast")
                case _:
                    print("Insane")
wpm(input(), int(input()))
