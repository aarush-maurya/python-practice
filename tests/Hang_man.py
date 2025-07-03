import random

print(f"HANGMAN GAME")
print()
list_of_words = ["apple", "mango", "banana", "papaya", "kiwi", "tomato", "carrot"]
word = random.choice(list_of_words)
alpha_done = []
life = 6

def show():
    all_alpha = True
    for i in word:
            if i in alpha_done:
                print(i ,end =" ")
            else:
                print("_",end = " ")
                all_alpha = False
    print()
    return all_alpha
while True:
    
    if show():
        print("Congratulations ,you won")
        break
    print(f"You have {life} lives")
    alpha = input(f"Choose an alphabet\n --> ").strip().lower()
    print()
    if len(alpha) != 1 or alpha.isalpha() == False:
        print("You should type only a letter")
        continue
    elif alpha in alpha_done:
        print(f"You have already guessed {alpha} letter. Try another one")
        continue
    alpha_done.append(alpha)
    if alpha in word:
        print(f"Congratulations, you found a letter!")
        
        show()

        print()
        print()
    else:
        if life <=1:
            print("You lost , try again later")
            print(f"The word was {word}")
            exit()
        else:
            print("Oh no, the letter isnt there in the word")
            show()
            print()
            print()
            life -= 1
            print(f"Remaining lives: {life}")
            print()
            