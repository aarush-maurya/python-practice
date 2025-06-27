from getpass import getpass as input
while True:
    print(f"\033[31m===Rock, Paper, Scissors!===\033[0m")
    print(f"Choose R,P or S")
    pl_1 = input(f"Player 1 move :")
    pl_2 = input(f"Player 2 move : ")
    if pl_1 == pl_2:
        print(f"Draw!")
        exit()
    elif pl_1 == 'R':
        if pl_2=='P':
            win= '2'
        elif pl_2 == 'S':
            win ='1'
        else:
            print(f"You have to type 'R' ,'P' or 'S'")
            exit()
    elif pl_1 == 'P':
        if pl_2 == 'R':
            win = '1'
        elif pl_2 == 'S':
            win ='2'
        else:
            print(f"You have to type 'R' ,'P' or 'S'")
            exit()
    elif pl_1 == 'S':
        if pl_2 == 'R':
            win = '2'
        elif pl_2 == 'P':
            win ='1'
        else:
            print(f"You have to type 'R' ,'P' or 'S'")
            exit()
    else:
        print(f"You have to type 'R' ,'P' or 'S' ")
        exit()
    print(f"Winner is player {win}")
    try_ = input(f"Do you wanna try again?(yes/no) : ")
    while try_ != 'yes' and 'no':
        print(f"You either have to say 'yes' or 'no'")
        try_ = input(f"Do you wanna try again?(yes/no) : ")
        break
    if try_ != 'yes':
        break
