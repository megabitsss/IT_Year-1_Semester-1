"""Filter"""
import json
def student_fiter(student_dict, min_score):
    """Filter student who does not exceed minimum score"""
    passed_dict = {}
    for key, value in student_dict.items():
        if value >= min_score:
            passed_dict[key] = value
    if not passed_dict: #{ empty dict }
        print("Nope")
    else:
        for student, score in sorted(passed_dict.items()):
            print(f"{student}\t{score:.2f}")
student_fiter(json.loads(input()), float(input()))
