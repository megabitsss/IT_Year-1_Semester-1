"""boomerang"""
import math

def func1(x):
    """func1"""
    return x+1
def func2(y):
    """func2"""
    return 7*(y**3) + 2*(y**2) - 31*y + 1
def func3(z):
    """func3"""
    return z * -1
def func4(x, y):
    """func4"""
    return (x+y) * (x-y)
def func5(x, y, z):
    """func5"""
    return (y - math.sqrt(y**2 - 4*x*z)) / (2*x)
def main(x, y, z):
    """main func"""
    print(func1(x))
    print(func2(y))
    print(func3(z))
    print(func4(x, y))
    print(func5(x, y, z))

main(int(input()), int(input()), int(input()))
