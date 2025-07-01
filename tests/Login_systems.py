import time, os

login = f"\033[34m=\033[0m=\033[31m=\033[33mLOGIN\033[0m\033[34m=\033[0m=\033[31m=\033[0m"
register = f"\033[34m=\033[0m=\033[31m=\033[33mREGISTER\033[0m\033[34m=\033[0m=\033[31m=\033[0m"


logo = f"\033[35m=\033[0m=\033[31m=\033[1m\033[4m\033[33m YOUR COMPANY\033[0m\033[35m=\033[0m=\033[31m=\033[0m"


username = f"\033[36m\033[1mUSERNAME: \033[0m"
password = f"\033[36m\033[1mPASSWORD: \033[0m"
user = ""
users = {}#you can add users herre
verified = f"\033[1m\033[32mWELCOME {user}!\033[0m"
non_verified = f"\033[1m\033[33mPLEASE REGISTER!\033[0m"
pass_wrong = f"\033[1m\033[31mWRONG PASSWORD, PLEASE TRY AGAIN!\033[0m"
is_reg = f"\033[34m\033[1mDo you want to register? (yes/no) : \033[0m"

while True:
    print(f"{login:^100}")
    print(f"{logo:^108}")
    user = input(f"{username:>20}")
    passwd = input(f"{password:>20}")

    if user in users and users[user] == passwd:
        print(f"{verified:^100}")
        break

    elif user not in users :
        print(f"{non_verified:^100}")
        reg = input(f"{is_reg:>30}")
        if reg.capitalize() == "Yes":
            time.sleep(1)
            os.system("cls")
            print(f"{register:^100}")
            n_user = input(f"{username:>20}")
            n_passwd = input(f"{password:>20}")
            if n_user in users:
                print(f"\033[1m\033[31mTHIS USER IS ALREADY REGISTERED!\033[0m")
            else:
                print(f"\033[1m\033[32mSuccessfully Registered as {n_user}!\033[0m")
                time.sleep(3)
                os.system("cls")
                print(f"{login:^100}")
                users[n_user] = n_passwd
                continue
        elif reg.capitalize() == "No":
            exit()
        else:
            while True:
                print(f"You either have to state 'Yes' or 'No' ")
                reg = input(f"{is_reg:>30}")
                

    elif user in users and users[user] != passwd:
        print(f"{pass_wrong:^100}")
        time.sleep(2)
        os.system("cls")
        continue
