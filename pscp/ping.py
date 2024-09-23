"""ping"""
import math
def ping_stats():
    """showing ping statistics from those 4 packets"""
    folder = input()
    _ = input()
    pinging = input()
    most = math.inf * -1
    least = math.inf
    if "[" in pinging:
        start = pinging.index("[") + 1
        stop = pinging.index("]")
        ip = pinging[start:stop]
    else:
        start = folder.index("ping") + len("ping") + 1
        ip = folder[start:]
    received = 0
    lost = 0
    avg = 0
    for _ in range(4): #packet inputs
        packet = input()
        if "Reply" in packet: #แสดงว่ามีการส่ง
            received += 1
            start = packet.index("time") + 5
            logic_operator = packet[packet.index("time")+4]
            stop = packet.index("ms")
            speed = int(packet[start:stop])
            if logic_operator == "<": #แสดงว่า speed = 0
                speed = 0
            else:
                speed = int(packet[start:stop])
            most = max(speed, most)
            least = min(speed, least)
            avg += speed #haven't divided by received yet
        else: #failed
            lost += 1
    if received > 0:
        avg = avg // received
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {received}, Lost = {lost} ({lost/4 *100:.0f}% loss),")
    if lost < 4:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {least}ms, Maximum = {most}ms, Average = {avg:.0f}ms")
ping_stats()
