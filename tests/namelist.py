names = []
while True:
    first_name = input(f"Enter your  first name : ")
    last_name = input(f"Enter your last name :  ")
    name = f"{first_name.strip().capitalize()} {last_name.strip().capitalize()}"
    if name in names:
        print(f"The {name} is already in the list\n ")
        continue
    else:
        names.append(name)
        print(f"{name} is added to the list\n")