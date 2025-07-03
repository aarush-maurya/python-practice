print(f"RAINBOW-NISER")
my_str = input(f"Enter the sentence you want to rainbow-nise\n-->")
print()
for i in my_str:
    if i.lower() == "r":
        print(f"\033[31m", end = "")
    elif i.lower() == 'g':
        print(f"\033[32m", end = "")
    elif i.lower() == 'y':
        print(f"\033[33m", end = "")
    elif i.lower() == "b":
        print(f"\033[34m", end = "")
    elif i.lower() == " ":
        print(f"\033[0m", end = "")
    print(i, end = "")
    print("\033[0m" , end = "")