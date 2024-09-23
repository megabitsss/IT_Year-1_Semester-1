"""jumping"""
def main():
    """main func"""
    jumping()
def jumping():
    """4 times calling another func"""
    print_output(1)
    print_output(2)
    print_output(3)
    print_output(4)
def print_output(num):
    """printing func"""
    print(f"Output{num}\nOutput{num}\nOutput{num}")
main()
