"""save compute repeat"""
def main():
    """"main func"""
    start_here =492137954293754252786
    millisceonds = start_here
    seconds = millisceonds//1000
    millisceonds = millisceonds %1000
    minutes = seconds//60
    seconds = seconds%60
    hours = minutes //60
    minutes = minutes%60
    days =hours//24
    hours = hours%24
    print(days,hours,minutes,seconds,millisceonds)

main()
