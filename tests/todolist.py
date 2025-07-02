import os, time
my_list = []
def print_list():
    os.system("cls")
    list_title = f"\033[34m=\033[0m=\033[31m=\033[33;1mLIST\033[0m\033[34m=\033[0m=\033[31m=\033[0m"
    print(f"{list_title: ^100}")
    for index in range(len(my_list)):
        printed_list = (f"\033[36;1m{index}) {my_list[index]}\033[0m")
        print(f"{printed_list: <100}")
    time.sleep(1)
        
title = f"\033[34m=\033[0m=\033[31m=\033[33;1mTODO-LIST\033[0m\033[34m=\033[0m=\033[31m=\033[0m"
while True:
    print(f"{title: ^100}")
    fb = input("\033[93mDo you want to 'add','view','remove' or 'edit' the list\n-->\033[0m")
    if fb == 'add':
        add_item = input(f"\033[34;1mEnter your task to be added to the list\n-->\033[0m")
        if add_item in my_list:
            warn_already = (f"\033[31;1m{add_item} is aleady in the list, you cant add dublicate tasks!\033[0m")
            print(f"{warn_already: ^100}")
            time.sleep(3)
            os.system("cls")
        else:
            my_list.append(add_item)
            added = (f"\033[32;1m{add_item} added to todo list!\033[0m")
            print(f"{added: ^100}")
            time.sleep(1)
            os.system("cls")
    elif fb == 'view':
        print_list()
    elif fb == 'remove':
        rem_item = input("\033[33;1mEnter the task to be removed\n-->\033[0m")
        if rem_item in my_list:
            confirm = input(f"\033[31;1mAre you sure you want to remove '{rem_item}' from the list?(type 'YES' or anythin else to cancel)\033[0m\n-->")
            if confirm == "YES":
                my_list.remove(rem_item)
                rem = (f"\033[31;1m{rem_item} is removed from todo list!\033[0m")
                print(f"{rem : ^100}")
                time.sleep(1)
                os.system("cls")
            else:
                continue
        else:
            warn_not = (f"\033[31;1m{rem_item} is not in the list\033[0m")
            print(f"{warn_not : ^100}")
            time.sleep(1)
            os.system("cls")
    elif fb == "edit":
        edit_item = input("\033[33;1mEnter the item you want to edit\033[0m\n-->")
        if edit_item in my_list:
            my_list.remove(edit_item)
            new = input("\033[31;1mEnter the new item to be replaced\033[0m\n-->")
            my_list.append(new)
        else:
            print(f"{warn_not : ^100}")
            time.sleep(1)
            os.system("cls")
            
    else:
        err = (f"\033[91;1;4mYou have to state 'add' , 'view' ,'remove' or 'edit'\033[0m")
        print(f"{err: ^100}")
        time.sleep(3)
        os.system("cls")
