# """Saint Seiya"""
# def punch_counter(duration, punch_limit):
#     """Count Seiya's punches"""
#     punch_cnt = 0
#     rolling = False
#     for second in range(1, duration+1):
#         # if not second or second % 2: #we do not need zero second
#         #     continue
#         if punch_cnt >= punch_limit:
#             if not rolling:
#                 rolling = True
#             else:
#                 punch_left = (duration - second + 1) * 12
#                 punch_cnt += punch_left
#                 break
#         else:
#             if not second % 6:
#                 punch_cnt += 1
#             elif not second % 2:
#                 punch_cnt += 165
#     print(punch_cnt)
# punch_counter(int(input()), int(input()))
def seiya(second, punch):
    punches = 0
    for i in range(2, second+1, 2):
        if punches < punch:
            if not i % 6:
                punches += 1
            elif not i % 2:
                punches += 165
        else:
            punches += (second+1 - i) * 12
            break
    print(punches)
seiya(int(input()), int(input()))