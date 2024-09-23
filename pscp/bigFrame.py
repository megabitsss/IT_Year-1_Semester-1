"""big frame"""
def text_frame():
    """put those texts in the frame"""
    txt_1 = input().strip()
    txt_2 = input().strip()
    txt_3 = input().strip()
    txt_4 = input().strip()
    txt_5 = input().strip()
    maxLen = max(len(txt_1), len(txt_2), len(txt_3), len(txt_4), len(txt_5))
    print("*" * (maxLen + 4))
    print("* "+ txt_1 + " "*(maxLen-len(txt_1))+" *")
    print("* "+ txt_2 + " "*(maxLen-len(txt_2))+" *")
    print("* "+ txt_3 + " "*(maxLen-len(txt_3))+" *")
    print("* "+ txt_4 + " "*(maxLen-len(txt_4))+" *")
    print("* "+ txt_5 + " "*(maxLen-len(txt_5))+" *")
    print("*" * (maxLen + 4))
text_frame()

#expected
# ***************
# * Hello World *
# * in          *
# * a           *
# * big         *
# * frame       *
# ***************

# ***************
# * Hello World *
# * in          *
# * a           *
# * big         *
# * frame       *
# ***************
