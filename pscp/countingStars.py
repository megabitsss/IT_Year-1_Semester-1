"""counting stars"""
def star_counter(stars):
    """count those stars"""
    constellation = 0
    comet = 0
    shooting = 0
    star_concat = ""
    for star in stars:
        star_concat += star
        if "~*" in star_concat:
            comet += 1
            star_concat = ""
        elif "*~" in star_concat:
            comet += 1
            star_concat = ""
        elif "*/" in star_concat:
            shooting += 1
            star_concat = ""
        elif "**" in star_concat:
            constellation += 1
            star_concat = ""
        if len(star_concat) == 3: #ถ้ามาสองอันแล้วไม่เข้าเกณฑ์ ก็รีเซ็ทเลยเพราะยังไงไม่ได้ใช้
            star_concat = star_concat[-1] #/* ""
        if star_concat == " ": #if only 1 blank, just res3t it
            star_concat = ""
    if comet or constellation or shooting: #no zero
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting}")
    else:dsdadasdahello world
        print("Tonight is a quiet night.")
star_counter(input())
#ใช้ count มันจะมีเคสแบบนี้ ~*~
#~* */ */ / * **
#~~*
