"""Dart"""
def dart_cal(n):
    """calculate the dart score"""
    score = 0
    for _ in range(n):
        x, y = map(int, input().split())
        distance = (x**2 + y**2)**0.5
        match distance:
            case distance if distance <= 2:
                score += 5
            case distance if distance <= 4:
                score += 4
            case distance if distance <= 6:
                score += 3
            case distance if distance <= 8:
                score += 2
            case distance if distance <= 10:
                score += 1
    print(score)
dart_cal(int(input()))
