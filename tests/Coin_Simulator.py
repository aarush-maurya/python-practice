import random
def color(a , b):
    a = str(a)
    if b == 'red':
        print(f"\033[31m{a}\033[0m")
    elif b == 'green':
        print(f"\033[32m{a}\033[0m")
        
flip_number = int(input(f"Enter the number of times you want to flip the coin :  "))
Head = 0
Tail = 0
def toss():
    flip = random.randint(1,2)
    if flip == 1:
        flip = 'Head'
        global Head
        Head += 1
    else:
        flip = 'Tail'
        global Tail
        Tail += 1
    print(flip)
for i in range(flip_number):
    toss()
color("===Occurance===", "red")
print(f"Heads have occurred {Head} times, approx {round((Head/flip_number)*100, 3)}%")
print(f"Tails have occurred {Tail} times, approx {round((Tail/flip_number)*100, 3)}%")
