"""four directions"""
def arrow_type_u_d(arrow_type, row):
    """return an arrow without space gaps"""
    match arrow_type:
        case "U":
            match row:
                case 1 | 4 | 5:
                    return "  *  "
                case 2:
                    return " *** "
                case 3:
                    return "* * *"
        case "D":
            match row:
                case 1 | 2 | 5:
                    return "  *  "
                case 3:
                    return "* * *"
                case 4:
                    return " *** "
def arrow_type_l_r(arrow_type, row):
    """return an arrow without space gaps"""
    match arrow_type:
        case "L":
            match row:
                case 1 | 5:
                    return "  *  "
                case 2 | 4:
                    return " *   "
                case 3:
                    return "*****"
        case "R":
            match row:
                case 1 | 5:
                    return "  *  "
                case 2 | 4:
                    return "   * "
                case 3:
                    return "*****"
def main(arrow_key):
    """main process of creating an arrow"""
    for row in range(1, 6):
        for letter in arrow_key:
            if letter in ("U", "D"):
                print(arrow_type_u_d(letter, row), end=" ")
            else:
                print(arrow_type_l_r(letter, row), end=" ")
        print()
main(input())
