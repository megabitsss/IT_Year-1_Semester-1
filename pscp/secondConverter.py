"""second converter"""
def main(k, s, m, h): #k=input, s=1 minute, m=1hr, h=1day
    """main func"""
    second = k%s
    minute = k//s
    hour = minute//m
    minute = minute%m
    hour %= h
    print(f"{hour}:{minute}:{second}")
main(int(input()), int(input()), int(input()), int(input()))
