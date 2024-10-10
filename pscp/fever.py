"""Fever"""
def fever_check(temp):
    """check level of user's fever"""
    match temp:
        case temp if 36 <= temp < 38:
            print("No Fever")
        case temp if 38 <= temp < 39:
            print("Mild Fever")
        case temp if 39 <= temp < 40:
            print("High Fever")
        case temp if temp >= 40:
            print("Very High Fever")
fever_check(float(input()))
