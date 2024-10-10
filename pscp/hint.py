"""hint"""
def comparator(txt):
    """return a list from the following comparator"""
    num = txt[-1]
    if "==" in txt:
        return [num]
    elif "!=" in txt:
        return list(range(0, num), range(num+1, 10))
def main():
    """main process of giving a hint to the uncle"""
    units_list = comparator(input())
    tens_list = comparator(input())
    hundreds_list = comparator(input())