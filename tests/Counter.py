import time, os

print(f"\033[32m===Counter===\033[0m")
a = int(input(f"Enter the starting number: "))
b = int(input(f"Enter the ending number: "))
c = int(input(f"Enter the size of increment: "))
d = float(input(f"Enter the duration of how fast counting should be done (in sec) : "))
print("\033[?25l")
if b>a:
    for i in range(a,(b+1),c):
        print(f"{i: ^100}") #you can adjust this print
        time.sleep(d)
        os.system("cls")
elif a>b:
    for i in range(a,(b-1),c):
        print(f"{i: ^100}") #you can adjust this print
        time.sleep(d)
        os.system("cls")
print("\033[?25h")