import random
import os
import time

# Roll a dice with 'a' sides
def roll(a):
    dice = random.randint(1, a)
    return dice

# Generate health stat
def health():
    health_stat = ((roll(6) * roll(12)) / 2) + 10
    return health_stat

# Generate strength stat
def strength():
    strength_stat = ((roll(6) * roll(8)) / 2) + 12
    return strength_stat

# Start round count
round = 1

# --- Character 1 Creation ---
while True:
    print(f"\033[32m✨Character Builder✨\033[0m")
    name_1 = input("Enter your character's name: ")
    char_type_1 = input("Enter your character type(Human, Elf, Wisard, Orc...): ")
    st_1 = strength()
    ht_1 = health()
    print(f"STRENGTH: {st_1}")
    print(f"HEALTH  : {ht_1}")
    print("May your name go down in legend...")

    replay = input("Do you want to build again? (Yes/No): ")
    if replay.capitalize() == "Yes":
        time.sleep(1)
        os.system("cls")
        continue
    elif replay.capitalize() == "No":
        break
    else:
        while True:
            print("You either have to type 'Yes' or 'No'")
            replay = input("Do you want to build again? (Yes/No): ")
            if replay.capitalize() == "Yes":
                os.system("cls")
                break
            elif replay.capitalize() == "No":
                break

# --- Character 2 Creation ---
while True:
    print(f"\033[32mWho is this going to FIGHT?✨\033[0m")
    name_2 = input("Enter your character's name: ")
    char_type_2 = input("Enter your character type(Human, Elf, Wisard, Orc...): ")
    st_2 = strength()
    ht_2 = health()
    print(f"STRENGTH: {st_2}")
    print(f"HEALTH  : {ht_2}")
    print("May your name go down in legend...")

    replay = input("Do you want to build again? (Yes/No): ")
    if replay.capitalize() == "Yes":
        time.sleep(1)
        os.system("cls")
        continue
    elif replay.capitalize() == "No":
        break
    else:
        while True:
            print("You either have to type 'Yes' or 'No'")
            replay = input("Do you want to build again? (Yes/No): ")
            if replay.capitalize() == "Yes":
                os.system("cls")
                break
            elif replay.capitalize() == "No":
                break

# --- Fight Introduction ---
print(f"\nAt one side, we have \033[34m{name_1}\033[0m, a skilled \033[32m{char_type_1}\033[0m, known for unmatched power.")
time.sleep(2)
print(f"On the other side, there's \033[31m{name_2}\033[0m, a fierce \033[32m{char_type_2}\033[0m, feared by all.\n")
time.sleep(3)

print(f"\033[36mFirst Round!\033[0m")
time.sleep(1)
print(f"\033[33m1...\033[0m")
time.sleep(1)
print(f"\033[33m2...\033[0m")
time.sleep(1)
print(f"\033[33m3...\033[0m")
time.sleep(1)
print(f"\033[33mFIGHT!\033[0m\n")
time.sleep(1)

# --- Battle Loop ---
while True:
    round += 1
    print(f"\033[36m--- ROUND {round} ---\033[0m")
    win_number_1 = roll(6)
    win_number_2 = roll(6)

    # Decide attacker and defender
    if win_number_1 > win_number_2:
        winner = name_1
        loser = name_2
        attacker_strength = st_1
        defender_health = ht_2
        defender_name = name_2
    else:
        winner = name_2
        loser = name_1
        attacker_strength = st_2
        defender_health = ht_1
        defender_name = name_1

    # Damage calculation
    dmg = int((abs(st_1 - st_2) + 1) * roll(2))

    # Announce attack
    print(f"{winner} strikes {loser} and deals {dmg} damage!")

    # Apply damage
    if winner == name_1:
        ht_2 -= dmg
        if ht_2 <= 0:
            break
        else:
            print(f"{loser} survives with {ht_2} health.\n")
    else:
        ht_1 -= dmg
        if ht_1 <= 0:
            break
        else:
            print(f"{loser} survives with {ht_1} health.\n")

    time.sleep(4)

# --- Victory Message ---
time.sleep(1)
print(f"\n\033[35mAnd the winner is...\033[0m")
time.sleep(2)
print(f"\033[1;32m🏆 {winner.upper()} WINS THE BATTLE! 🏆\033[0m\n")
