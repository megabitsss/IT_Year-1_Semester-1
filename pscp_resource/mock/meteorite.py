"""meteorite"""
def main(total_kg, sub_kg, threshold):
    """main"""
    cnt = 0
    division = 1
    while True:
        if total_kg >= threshold:
            cnt += division
            total_kg /= sub_kg
        else:
            break

        match division: ###
            case 1:
                division = sub_kg
            case _:
                division *= sub_kg
    print(cnt)
main(float(input()), int(input()), float(input()))
