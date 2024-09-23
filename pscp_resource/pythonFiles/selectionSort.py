"""selection sort"""
def selection_sorted(num):
    """sort the number selectionly"""
    num_list = list(num)
    for i in range(0, len(num_list)-1): #range(0, 4) -> 0,1,2,3
        min_index = i
        for j in range(i+1, len(num_list)): #อันนี้ต้องเอาไปเช็คถึงตัวท้าย
            if num_list[j] < num_list[min_index]:
                min_index = j #เก็บค่า index ที่เจอไว้ว่าอยู่ตำแหน่งไหน
        if min_index != i: #min_index ถูกเปลี่ยน
            num_list[i], num_list[min_index] = num_list[min_index], num_list[i] #swapping เอาตัวน้อยสุดมาไว้ด้านหน้า
    print(num_list)
selection_sorted(input())
# #1, 2, 7, 4, 5
def test(num):
    num_list = list(num)
    for i in range(0, len(num_list)-1):
        min_index = i
        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[min_index]:
                min_index = j
        if min_index != i:
            num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    print(num_list)
test(input())
#3, 3, 4, 1 (0 to 2) -> range(0, 3)