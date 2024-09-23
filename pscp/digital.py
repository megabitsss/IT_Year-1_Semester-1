"""digital"""
def digital_qualifier():
    """qualify for your digital money"""
    name = input()
    thai = input()
    home = input()
    age = float(input())
    salary = float(input())
    deposit = float(input())
    nationality_home = thai in ("Yes", "True") and home in ("Yes", "True")
    if nationality_home and age >= 16 and salary <= 840_000 and deposit <= 500_000:
        print(f"Congratulations! {name} is qualified to receive a digital wallet amount of \
10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
digital_qualifier()
