"""Ascend the number"""
def ascender():
    """ascend the array"""
    nums = []
    while True:
        num = input()
        if num == "END":
            break
        num = int(num)
        nums.append(num)
    while True:
        swap = False
        for index in range(len(nums)-1):
            if nums[index] > nums[index+1]:
                nums[index], nums[index+1] = nums[index+1], nums[index] #Swapping
                swap = True
        if not swap:
            break
    print(*nums, sep="\n")
ascender()
