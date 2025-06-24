# 6: Custom Affirmation Generator
print("\033[32m=== Affirmation Generator ===\033[0m")
name = input("What's your name? ")
rate = int(input("Rate your day from 1 to 10: "))
place = input("Favorite place? ")
food = input("Favorite food? ")
season = input("Favorite season? ")
if rate == 1:
    print("So sorry to hear that,", name)
elif rate < 5:
    print("Tough day, huh? You'll get through it.")
elif rate == 5:
    print("Right in the middle, let's lift it up!")
elif rate > 5:
    print("Glad you're having a better day!")
if rate == 10:
    print("Awesome! Your best day!")
print(f"Now imagine you're enjoying {food} in {place} during {season} — sounds nice?")

# 7: Score Checker
print("\033[32m=== Score Checker ===\033[0m")
score = int(input("Enter your score: "))
if score >= 1000:
    print("Congratulations, you won!")
else:
    print("You lost, try again!")
