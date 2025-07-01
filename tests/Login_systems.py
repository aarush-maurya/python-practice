title = f"\033[34m=\033[0m=\033[31m=\033[33mLOGIN\033[0m\033[34m=\033[0m=\033[31m=\033[0m"
print(f"{title: ^100}")
logo = f"\033[35m=\033[0m=\033[31m=\033[1m\033[4m\033[33mMATRIX SOCIETY\033[0m\033[35m=\033[0m=\033[31m=\033[0m"
print(f"{logo: ^100}")
username = f"\033[36m\033[1mUSERNAME: \033[0m"
password = f"\033[36m\033[1mPASSWORD: \033[0m"
user = ""
verified = f"\033[1m\033[32mWELCOME {user}!\033[0m "
non_verified = f"\033[1m\033[33mPLEASE REGISTER!\033[0m "
pass_wrong = f"\033[1m\033[31mWRONG PASSWORD, PLEASE TRY AGAIN!\033[0m "
is_reg = f"\033[34m\033[1mDo you want to register? (yes/no) : \033[0m"
while True:
    user = input(f"{username: >20}")
    passwd = input(f"{password: >20}")
    if user == "aarush" and passwd == "7781":
        print(f"{verified: ^100}")
        break
    elif user != "aarush":
        print(f"{non_verified: ^100}")
        reg = input(f"{is_reg: >30}")
        if reg.capitalize() == "Yes":
            print(f"\033[1m\033[31mSORRY, REGISTER FEATURE IS IN PROGRESS!\033[0m ")
        break
    elif user == "aarush" and passwd != "7781":
        print(f"{pass_wrong: ^100}")
        continue
        
