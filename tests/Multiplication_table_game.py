a = int(input(f"Enter the number you know multiplication table of : "))
point = 0
for i in range(1,11):
    ans = int(input(f"{a} X {i} = "))
    if ans == a*i:
        print(f"Good!")
        point += 1
    elif ans!= a*i:
        print(f"No!, the answer was {i*a}")
if point == 10:
    print(f"Hurray!, you got it all of them correctly! 10/10")
else:
    print(f"You got {point} points!")
