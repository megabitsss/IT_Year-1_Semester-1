"""Roman"""
def roman2arabic(roman):
    """Convert from roman number to arabic number"""
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic = 0
    roman = roman.replace("IV", "IIII")
    roman = roman.replace("IX", "VIIII")
    roman = roman.replace("XL", "XXXX")
    roman = roman.replace("XC", "LXXXX")
    roman = roman.replace("CD", "CCCC")
    roman = roman.replace("CM", "DCCCC")
    for letter in roman:
        arabic += roman_dict[letter]
    print(arabic)
roman2arabic(input())
