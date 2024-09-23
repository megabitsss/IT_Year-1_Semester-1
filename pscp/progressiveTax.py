"""progressive tax"""
def tax_cal(cash):
    """calculating the taxes"""
    match cash: #money you've got
        case 300_000:
            return (300_000 - 150_000) * 0.05
        case 500_000:
            return (500_000 - 300_000) * 0.1 + tax_cal(300_000)
        case 750_000:
            return (750_000-500_000) * 0.15 + tax_cal(500_000)
        case 1_000_000:
            return (1_000_000-750_000) * 0.2 + tax_cal(750_000)
        case 2_000_000:
            return (2_000_000-1_000_000) * 0.25 + tax_cal(1_000_000)
        case 4_000_000:
            return (4_000_000-2_000_000) * 0.3 + tax_cal(2_000_000)
def main(salary):
    """main function"""
    tax = 0
    match salary:
        case s if 0 <= s <= 150_000:
            tax = 0
        case s if 150_000 <= s < 300_000:
            tax = (salary-150_000) * 0.05
        case s if 300_000 <= s < 500_000:
            tax = (salary-300_000) * 0.1 + tax_cal(300_000)
        case s if 500_000 <= s < 750_000:
            tax = (salary-500_000) * 0.15 + tax_cal(500_000)
        case s if 750_000 <= s < 1_000_000:
            tax = (salary-750_000) * 0.2 + tax_cal(750_000)
        case s if 1_000_000 <= s < 2_000_000:
            tax = (salary-1_000_000) * 0.25 + tax_cal(1_000_000)
        case s if 2_000_000 <= s < 4_000_000:
            tax = (salary-2_000_000) * 0.3 + tax_cal(2_000_000)
        case _: #equivalent to else condition
            tax = (salary-4_000_000) * 0.35 + tax_cal(4_000_000)
    print(int(tax))
main(int(input()))
