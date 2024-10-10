"""T-Score"""
import math
def t_score_cal(n, max_score):
    """calculate t-score"""
    max_score += 0
    students_score = [int(input()) for _ in range(n)]
    sum_score = sum(students_score)
    sum_score_squared = sum(student**2 for student in students_score)
    avg = sum_score / n
    sd = math.sqrt((n * sum_score_squared - sum_score**2) / (n*(n-1)))
    if not sd: #sd == 0
        z_score = [0 for score in students_score]
    else:
        z_score = [(score - avg)/sd for score in students_score]
    t_score = [50 + 10*score for score in z_score]
    print(*([f"{score:.2f}" for score in t_score]), sep="\n")
t_score_cal(int(input()), int(input()))
