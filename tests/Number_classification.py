# 4: Number Classification
print("\033[32m=== Number Classification ===\033[0m")
num = int(input("Enter a number between 0 and 999: "))
if num < 0:
    print("Invalid Entry")
elif num < 10:
    print("Single digit number")
elif num < 100:
    print("Double digit number")
elif num <= 999:
    print("Triple digit number")
else:
    print("Number out of range")
