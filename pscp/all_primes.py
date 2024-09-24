"""All Primes"""
def is_prime(n):
    """check if the number is prime"""
    all_prime = [2, 3] #initial
    if n == 1:
        return False
    if n in all_prime:
        return True
    for i in all_prime:
        if not n % i:
            return False #หารลงตัว แสดงว่าไม่ใช่
    max_range = int(n ** 0.5) + 1
    divisor = all_prime[-1] + 2 #+2 เพราะตัวมากสุดใน prime หารแล้วยังไม่ลงตัว เลยเอาเลขคี่ตัวต่อไป
    while divisor <= max_range:
        if is_prime(divisor): #เลขตัวนั้นเป็น Prime (ความจริงโปรแกรมเราแค่ cnt ไม่จำเป็นต้องทำก็ได้)
            all_prime.append(divisor)
        if not n % divisor: #ถ้าเจอตัวไหนที่หารแล้วลงตัวปุ๊ป
            return False
        divisor += 2
    return True
def coutner(n):
    """count prime number from 1 to n"""
    cnt = 0
    for number in range(1, n+1):
        if is_prime(number):
            cnt += 1
    print(cnt)
coutner(int(input()))
