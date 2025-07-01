print("Thirty days down, what do you think?")
print()
for i in range(1, 30):
    thought = input(f"So, what was your thought for day {i}? :  ")
    print()
    my_text = (f"So your thought of day {i} was:\n")
    print(f"{my_text: ^60}")
    print(f"{thought: ^60}")
    print()