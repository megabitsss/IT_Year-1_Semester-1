"""US Interstate Number System"""
def major_2(str_num):
    """major 2"""
    if str_num[-1] == "5":
        return "Vertical"
    if str_num[-1] == "0":
        return "Horizontal"
    return "Others"
def printing(interstate_type, m_type, interstate_num):
    """printing"""
    if not interstate_type == "Others":
        print(f"{interstate_type} {m_type} Interstate")
        print(f"I-{interstate_num}")
    else:
        print("Others")
def interstate_finder(num):
    """find the interstate"""
    interstate_type = ""
    m_type = ""
    interstate_num = num #default for major
    str_num = str(num)
    if len(str(num)) == 3: #Minor
        m_type = "Minor"
        interstate_num = int(str_num[1:])
        if not int(str_num[0]) % 2: #Even
            interstate_type = "Even"
            if not str_num[-1] in ("0", "5"): #not the interstate
                interstate_type = "Others"
        else:
            interstate_type = "Odd"
            if not str_num[-1] in ("0", "5"): #not the interstate
                interstate_type = "Others"
        if not (str_num[-1] in ("0", "5")) or str_num[-2:] == "00": #Not in the interstate
            interstate_type = "Others"
    elif 1 <= len(str_num) <= 2: #Major
        m_type = "Major"
        if len(str_num) == 2:
            interstate_type = major_2(str_num)
        elif len(str_num) == 1:
            if str_num[-1] == "5":
                interstate_type = "Vertical"
                interstate_num = "5"
            else:
                interstate_type = "Others"
    else:
        interstate_type = "Others"
    printing(interstate_type, m_type, interstate_num)
interstate_finder(int(input()))
#05 -> Output must be I-5 not I-05
#100 -> interstate สองตัวท้ายจะไม่มี 00 -> Others
