"""jump around"""
def func1(x):
    """func1"""
    return x
def func2(x):
    """func2"""
    return x + 5
def func3(x):
    """func3"""
    return x - 17
def func4(x):
    """func4"""
    return x * 32
def func5(x):
    """func5"""
    return 5*(x**2) + 50*x + 3
def main(x):
    """main func"""
    print(func1(x))
    print(func2(x))
    print(func3(x))
    print(func4(x))
    print(func5(x))
main(int(input()))
