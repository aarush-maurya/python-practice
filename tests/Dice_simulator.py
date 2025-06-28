import random 
roll_amt= int(input(f"Enter the number of times you want to roll the Dice: "))
i = 1
six = 0
def rollDice():
    global i,six
    roll = random.randint(1,6)
    if roll == 6:
        six +=1
    print(f"{i}.You have rolled {roll}")

for i in range (roll_amt):
    rollDice()
    i+= 1
print(f"\033[31m===Occurance of 6===\033[0m")
print(six)
print(f" that is {(six/roll_amt)*100}% for instance the percentage probability of occurace of 6 is {round(100/6, 3)}% ")