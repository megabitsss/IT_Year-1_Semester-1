"""lift"""
def lift_cal(n, lift_most_weight):
    """calculate if the lift/person are safe"""
    most_age = 0
    sigma_weight = 0
    for _ in range(n):
        age = int(input())
        weight = float(input())
        if age >= most_age:
            most_age = age
        sigma_weight += weight
    if most_age >= 12 and sigma_weight <= lift_most_weight or not n:
        print("Safe")
    else:
        print("Not Safe")
lift_cal(int(input()), float(input()))
