"""data spike"""
def main(new_num, current):
    """main func"""
    if new_num>current:
        return new_num
    return current
MAX = main(int(input()), 0)
MAX = main(int(input()), MAX)
MAX = main(int(input()), MAX)
MAX = main(int(input()), MAX)
MAX = main(int(input()), MAX)
MAX = main(int(input()), MAX)
MAX = main(int(input()), MAX)
MAX = main(int(input()), MAX)
print(MAX)
