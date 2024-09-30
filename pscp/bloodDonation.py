"""Blood Donation"""
def blood_cond():
    """checking for blood donation requirements"""
    age = int(input())
    weight = int(input())
    donated = int(input())
    certified = True
    if age == 17 or (60 <= age <= 70):
        certified = input()
        if certified == "False":
            certified = False
    if not donated:
        donated = age <= 55
    age = 17 <= age <= 70
    weight = weight >= 45
    if age and weight and donated and certified:
        print("Yes")
    else:
        print("No")
blood_cond()
