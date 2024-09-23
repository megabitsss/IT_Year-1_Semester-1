"""brick bridge"""
def main(a, b, bridge): #a=small, b=big
    """main func"""
    max_b = bridge//5
    if b > max_b:
        b = max_b
    sumz = (b*5) + a
    if sumz >= bridge:
        used_a = bridge - (b*5)
        print(used_a)
    else:
        print("-1")
main(int(input()), int(input()), int(input()))
