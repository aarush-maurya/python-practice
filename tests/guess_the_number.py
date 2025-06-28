print(f"\033[31m===Guess: One-Million-to-one===\033[0m")
number = 983724
i = 1
while True:
    guess = int(input(f"Guess the number (from 0 to 1000000) : "))
    if guess == number:
        break
    elif  1000000 < guess :
        print(f"Your guess is larger than a million")
        print(F"Try again")
        exit()
    elif guess<0:
        print(f"Your guess can not be in negative")
        print(f"Try again!")
        exit()
    elif guess < number:
        print("The number is larger")
        i += 1
        continue
    elif guess > number:
        print(f"the number is smaller")
        i+=1
        continue
    else:
        print("Invalid syntax")
        exit()
print("\033[32mContragtulations!\033[0m, you have won the game")
print(f"Number of attempts :\033[33m{i}\033[0m")