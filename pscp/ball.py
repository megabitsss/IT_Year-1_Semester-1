"""ball"""
def main(height):
    """main func"""
    cnt = 0
    while height >= 0.01:
        height *= 3/5
        cnt += 1
    print(cnt-1)
main(float(input()))
