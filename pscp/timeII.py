"""time ii"""
def main(sec):
    """main func"""
    minute = sec // 60
    sec = sec - (minute*60)
    hrs = minute // 60
    minute = minute - (hrs*60)
    day = hrs // 24
    hrs = hrs - (day*24)
    if day <= 9999:
        print(f"{day:04}:{hrs:02}:{minute:02}:{sec:02}")
    else:
        print("ERR_:__:__:__")
main(int(input()))
