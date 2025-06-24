# 3: Login Systems
print("\033[32m=== Login System ===\033[0m")
user = input("Enter your username: ")
password = input("Enter your password: ")
if user == "Aarush" and password != "1234":
    confirm = input("Are you sure? (Yes/No): ")
    if confirm == "Yes":
        reason = input("Why do you think so? ")
        print("Still wrong password!")
    elif confirm == "No":
        print("Yeah, it's wrong.")
    else:
        print("Answer with Yes or No.")
elif user == "Aarush" and password == "1234":
    print("Access Granted!")
elif user != "Aarush":
    print("Please register!")