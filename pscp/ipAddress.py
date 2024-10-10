"""IP Address"""
def ip_checker(ip):
    """minimize the ip address or tells if it's valid/invalid"""
    for char in ip:
        if not char.isnumeric() and not char == ".": #เป็น false ทั้งคู่
            print("Invalid IPv4 address")
            return
    if ip.count(".") == 3:
        ip = ip.split(".")
        print(".".join(str(int(octet)) for octet in ip) if all(0 <= int(octet) <= 255 for octet in ip) else "Invalid IPv4 address")
    else:
        print("Invalid IPv4 address")
ip_checker(input())
