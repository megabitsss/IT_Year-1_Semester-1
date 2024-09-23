"""Saint Seiya"""
def punch_counter(duration, punch_limit):
    """Count Seiya's punches"""
    rolling_unlock = False
    if not punch_limit // 331: #แสดงว่าน้อยกว่า 6 วินาที -> loop ได้
        second_start = 1
        punch_cnt = 0
    else: #มากกว่า 6 วินาที (หา punch_limit ในปริมาณมาก ๆ)
        second_start = ((punch_limit // 331) * 6) + 1
        if duration > second_start:
            punch_cnt = (punch_limit // 331) * 331
        else:
            second_start = 1
            punch_cnt = 0
    if not punch_limit: #punch_limit = 0
        rolling_unlock = True
    for second in range(second_start, duration+1):
        if rolling_unlock:
            punch_cnt += (duration - 1) * 12
            break
        if not second % 6:
            punch_cnt += 1
        elif not second % 2:
            punch_cnt += 165
        if punch_cnt >= punch_limit and second < duration: #second < duration กันกรณีมาทำซ้ำ
            punch_cnt += (duration - second - 1) * 12
            break
    print(punch_cnt)
punch_counter(int(input()), int(input()))
