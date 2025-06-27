# a = "aarush"
# while True:
#     user = input(f"Enter your username : ")
#     if user == 'aarush':
#         break
#     else:
#         print(f"Wrong user, try again")

count = 0
while True:
    count += 1
    ans = input(f"Never going to ___ you up\n")
    if ans == 'give':
        print(f"Congratulations, you did it in {count} times.")
        break
    else:
        print(f"Nope, try again")