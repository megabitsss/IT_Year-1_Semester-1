"""compositeFunction"""
def main(x):
    """main func"""
    print(f"{fx(gx(x)):.2f}")
    print(f"{gx(fx(x)):.2f}")
def fx(x):
    """fx function"""
    return x * 2
def gx(x):
    """gx function"""
    return x/2 + 1
main(int(input()))
