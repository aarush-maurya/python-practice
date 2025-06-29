from getpass import getpass as input
pl1_w =0
pl2_w=0
while True:
    print(f"\033[31m===Rock, Paper, Scissors!===\033[0m")
    print(f"Choose R,P or S")
    pl_1 = input(f"Player 1 move :")
    pl_2 = input(f"Player 2 move : ")
    if pl_1 == pl_2:
        print(f"Draw!, you both types same things")
        continue
    elif pl_1.upper() == 'R':
        if pl_2.upper()=='P':
            win= '2'
            pl2_w += 1
        elif pl_2.upper() == 'S':
            win ='1'
            pl1_w += 1
        else:
            print(f"You have to type 'R' ,'P' or 'S'")
            exit()
    elif pl_1.upper() == 'P':
        if pl_2.upper() == 'R':
            win = '1'
            pl1_w += 1
        elif pl_2.upper() == 'S':
            win ='2'
            pl2_w += 1
        else:
            print(f"You have to type 'R' ,'P' or 'S'")
            exit()
    elif pl_1.upper() == 'S':
        if pl_2.upper() == 'R':
            win = '2'
            pl2_w += 1
        elif pl_2.upper() == 'P':
            win ='1'
            pl1_w += 1
        else:
            print(f"You have to type 'R' ,'P' or 'S'")
            exit()
    else:
        print(f"You have to type 'R' ,'P' or 'S' ")
        exit()
    print(f"Winner is player {win}")
    try_ = input(f"Do you wanna try again?(yes/no) : ")
    if try_ == 'yes':
        continue
    elif try_ == 'no':
        break
    while try_ != 'yes' and 'no':
        print(f"You either have to say 'yes' or 'no'")
        try_ = input(f"Do you wanna try again?(yes/no) : ")
        break
print(f"Player 1 has won {pl1_w} times and Player 2 has won {pl2_w} times")
    
        




