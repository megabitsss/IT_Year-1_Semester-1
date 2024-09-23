"""regulation"""
def main(a,b,c):
    """main func"""
    print(f"{a:>30}")
    print(f"{a:030}")
    print(f"{b:.2f}")
    print(f"{b:.12f}")
    print(f"{c:>40}")
main(int(input()),float(input()),input())
