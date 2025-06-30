import time, os

print(f"\033[32m===Counter===\033[0m")
a = int(input(f"Enter the starting number: "))
b = int(input(f"Enter the ending number: "))
c = int(input(f"Enter the size of increment: "))
d = float(input(f"Enter the duration of how fast counting should be done (in sec) : "))
if b>a:
    for i in range(a,(b+1),c):
        print(i)
        time.sleep(d
elif a>b:
    for i in range(a,(b-1),c):
        print(i)
        time.sleep(d)