# '''Solar System'''
# def main():
#     '''Note: the sun might differ'''
#     solarsys = input().strip()
#     solarsys = ' '+solarsys+' '
#     sunfin = solarsys.find(' Sun ')
#     leftspace = 0
#     rightspace = 0
#     spacecount = 0
#     for i,v in enumerate(solarsys):
#         if v == ' ':
#             spacecount += 1
#             if i == sunfin:
#                 leftspace = spacecount
#             elif i == sunfin + 4:
#                 rightspace = spacecount
#     leftlength = leftspace - 1
#     rightlength = spacecount - rightspace
#     cool = ''
#     if rightlength > leftlength:
#         cool += solarsys[solarsys.rfind(' ',0,len(solarsys)-1)+1:len(solarsys)]
#     elif leftlength > rightlength:
#         cool += solarsys[1:solarsys.find(' ',1)]
#     elif rightlength == leftlength:
#         cool += solarsys[1:solarsys.find(' ',1)] + ' '
#         cool += solarsys[solarsys.rfind(' ',0,len(solarsys)-1)+1:len(solarsys)]
#     hot = ''
#     if sunfin: # ->>>>>> มีทำไม ?
#         hot += solarsys[solarsys.rfind(' ',0,sunfin)+1:sunfin] + ' '
#     print(sunfin)
#     print(len(solarsys) - 1)
#     if sunfin != len(solarsys)-1:
#         hot += solarsys[sunfin+5:solarsys.find(' ',sunfin+5)]
#     print('Hot:',hot)
#     print('Cool:',cool)
#     print(f"{cool}|")
# main()
# #Sun Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
# #case นี้ปัญหาถ้าเอา if sunfin ออก

'''Solar System'''
def main():
    '''Note: the sun might differ'''
    solarsys = input().strip()
    solarsys = ' '+solarsys+' '
    sunfin = solarsys.find(' Sun ')
    leftspace = 0
    rightspace = 0
    spacecount = 0
    for i,v in enumerate(solarsys):
        if v == ' ':
            spacecount += 1
            if i == sunfin:
                leftspace = spacecount
            elif i == sunfin + 4:
                rightspace = spacecount
    leftlength = leftspace - 1
    rightlength = spacecount - rightspace
    cool = ''
    if rightlength > leftlength:
        cool += solarsys[solarsys.rfind(' ',0,len(solarsys)-1)+1:len(solarsys)]
    elif leftlength > rightlength:
        cool += solarsys[1:solarsys.find(' ',1)]
    elif rightlength == leftlength:
        cool += solarsys[1:solarsys.find(' ',1)] + ' '
        cool += solarsys[solarsys.rfind(' ',0,len(solarsys)-1)+1:len(solarsys)]
    hot = ''
    if sunfin:
        hot += solarsys[solarsys.rfind(' ',0,sunfin)+1:sunfin] + ' '
    if sunfin != len(solarsys)-1:
        print(solarsys.find(' ',sunfin+5))
        hot += solarsys[sunfin+5:solarsys.find(' ',sunfin+5)]
    print('Hot:',hot)
    print('Cool:',cool)
    print(f"{cool}|")
main()
