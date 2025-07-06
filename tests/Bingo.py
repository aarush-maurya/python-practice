import random,os,time
life = 3 
comp = 0
def create_card():
    nums = []
    for i in range(8):
        num = random.randint(1,90)
        if num in nums:
            while True:
                num = random.randint(1,90)
                if num not in nums:
                    break
        nums.append(num)
    sort = sorted(nums)
    card = [[sort[0], sort[1], sort[2]],
            [sort[3], "\033[33;1mBINGO\033[0m", sort[4]],
            [sort[5], sort[6], sort[7]]]
    return card
card = create_card()
def pretty_print(card):
    print()
    for row in card:
        for item in row:
            print(f"{item: ^5}",end = " \033[34;1m|\033[0m ")
        print()
        print("\033[34;1m-\033[0m"*23)
    print()
def even_count():
    count = 0
    for row in range(3):
        for item in range(3):
            if isinstance(card[row][item] , int) and card[row][item] % 2 ==0:
                count += 1
                
    return count
even_ = even_count()
pretty_print(card)
while True:
    found =False
    if life > 0:
        if comp < even_:
                num = int(input(f"Next number\n-->"))
                for row in range(3):
                    for item in range(3):
                        if isinstance(card[row][item], int) and card[row][item] % 2 == 0 and card[row][item] == num:
                            found = True
                            card[row][item] = "\033[31;1mX\033[0m"
                            comp+=1 
                            time.sleep(2)
                            os.system("cls")
                        elif isinstance(card[row][item], int) and card[row][item] % 2 != 0 and card[row][item] == num:
                            found = True
                            print("Wrong guess!")
                            life -= 1
                            print(f"Current Lives : {life}")
                            time.sleep(2)
                            os.system("cls")
                if found == False:
                    print("That number isnt in the card")
                    time.sleep(2)
                    os.system("cls")
                
                pretty_print(card)
        elif comp == even_ :
            print("You won")
            exit()
    else:
        print(f"You lost")
        break
