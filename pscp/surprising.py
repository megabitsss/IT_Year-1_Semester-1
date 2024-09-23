"""surprising vote"""
#force ให้คน 2 มากสุด -> คน 3 จะได้น้อยสุดๆ ถ้ายังไม่ surprising แสดงว่าไม่มีโอกาสละ
#ex. total=15, max=8 -> แสดงว่าจะเป็น 8,8,-1 เลยต้องใช้ max เหมือน clamp ไว้
def main(total, most):
    """main func"""
    lowest = total - (most+most)
    diff = most - max(0, lowest)
    if diff > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))

# second = min(total-high, high)
