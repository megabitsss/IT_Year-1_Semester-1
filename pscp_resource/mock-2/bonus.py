"""bonus"""
def bonus_finder(salary, year, month):
    """find bonus for the employee"""
    if month >= 10:
        year += 1
    if year > 20:
        year = 20
    bonus = salary * year
    if bonus > 1_000_000:
        bonus = 1_000_000
    elif bonus < 5_000:
        bonus = 5_000
    print(bonus)
bonus_finder(int(input()), int(input()), int(input()))
