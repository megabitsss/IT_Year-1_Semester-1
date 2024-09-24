"""OneTwo"""
def one_two(sn):
    """recursive function of sn"""
    if sn == 1:
        return "1"
    if sn == 2:
        return "2"
    return one_two(sn-1) + one_two(sn-2)
print(one_two(int(input())))
