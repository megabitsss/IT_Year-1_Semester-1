"""btsMrt"""
def train(day, age, height):
    """calculate train fee"""
    Senior = age >= 60 and day == "Senior Day"
    Child = age < 14 and height <= 140 and day == "Children Day"
    Child_Short = age < 14 and height < 90
    if Senior or Child or Child_Short:
        print("FREE")
    else:
        print("PAY")
train(input(), float(input()), float(input()))
