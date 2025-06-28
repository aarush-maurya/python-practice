print(f"\033[32m===Counter===\033[0m")
a = int(input(f"Enter the starting number: "))
b = int(input(f"Enter the ending number: "))
c = int(input(f"Enter the size of increment: "))
if b>a:
    for i in range(a,(b+1),c):
        print(i)
elif a>b:
    for i in range(a,(b-1),c):
        print(i)
