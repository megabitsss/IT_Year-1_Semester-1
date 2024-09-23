"""MAC"""
def hex_checker(hex_num):
    """check if the hexadecimal is valid"""
    hex_tup = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    def pattern1(hex_num):
        """checking for -"""
        if not len(hex_num) == 17:
            return False
        for char, number in list(zip(hex_num, range(1, 17))): #17 chars + 1
            if not ((not number % 3 and char == "-") or (number % 3 and char in hex_tup)):
                return False
        return True

    def pattern2(hex_num):
        """checking for :"""
        if not len(hex_num) == 17:
            return False
        for char, number in list(zip(hex_num, range(1, 18))): #17 chars + 1
            if not ((not number % 3 and char == ":") or (number % 3 and char in hex_tup)):
                return False
        return True

    def pattern3(hex_num):
        """checking for ."""
        if not len(hex_num) == 14:
            return False
        for char, number in list(zip(hex_num, range(1, 15))): #14 chars + 1
            if not ((not number % 5 and char == ".") or (number % 5 and char in hex_tup)):
                return False
        return True
    if pattern1(hex_num):
        print("VALID 1")
    elif pattern2(hex_num):
        print("VALID 2")
    elif pattern3(hex_num):
        print("VALID 3")
    else:
        print("ERROR")
hex_checker(input().lower())
