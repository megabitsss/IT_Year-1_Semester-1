"""Niwarn World"""
import math
def x(n):
    """function x"""
    number = 2 + ((math.log(n**2, 2))/(2*n*math.log(n, 2)))
    return number
def y(n, s):
    """function y"""
    number = (math.sin(math.radians(30)) + math.sqrt(2*s)) / (x(n) + 3)
    return number
def z(k):
    """function k"""
    number = (y(k, k))**2 + ((8456 * x(k)**4)/(24*k))
    return number
def niwarn_cal(n, s, k):
    """main proces of getting x, y, z values"""
    x_pos = x(n)
    y_pos = y(n, s)
    z_pos = z(k)
    print(f"X: {x_pos:.1f}, Y: {y_pos:.1f}, Z: {z_pos:.1f}")
niwarn_cal(float(input()), float(input()), float(input()))
