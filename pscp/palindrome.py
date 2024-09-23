"""palindrome"""
def clock(time):
    """changes minute and hour digit in a minute"""
    colon_index = time.find(":")
    hour = time[:colon_index]
    m1nute = time[colon_index+1:]
    m1nute = int(m1nute) + 1
    if m1nute == 60:
        hour = int(hour) + 1
        m1nute = "00"
    time = str(hour) + ":" + str(m1nute).rjust(2, "0") #zero padding for minute
    if time == "24:00":
        time = "0:00"
    return time
def palindrome_finder(n, time):
    """find the futer's palindrome number in amount 'n'"""
    while n > 0:
        time = clock(time)
        time_plain = time.replace(":", "")
        if time_plain == time_plain[::-1]:
            print(time)
            n -= 1
palindrome_finder(int(input()), input())
