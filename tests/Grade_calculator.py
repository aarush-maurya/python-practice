name = input(f"Enter the subject of exam : ")
max_mark = int(input(f"Write the Maximum Marks : "))
mark = float(input(f"Enter the marks that you got : "))
percentage = (mark/max_mark)*100
if percentage > 100:
    print(f"You cant get this much marks! Liar!")
    exit()
elif 100 == percentage >= 90:
    grade = 'A+'
elif 90 > percentage >= 80:
    grade ='A-'
elif 80> percentage >=70:
    grade = 'B'
elif 70> percentage >= 60:
    grade = 'C'
elif 60> percentage >=50:
    grade = 'D'
elif 50 > percentage:
    print(f"You are fail!, with {percentage}%")
    exit()
else:
    print(f"Invalid syntax bro")
    exit()
print(f"You got {round(percentage, 2)}%, and got {grade} grade ")
