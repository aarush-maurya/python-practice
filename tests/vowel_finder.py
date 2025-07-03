print(f"Vovel Finder")
str_ = input(f"Enter the string to detect vowels :  ")
vowel = "aeiou"
for i in str_:
    if i.lower() in vowel:
        print("\033[31;1m", end ="")
    print(i, end = "")
    print("\033[0m", end = "")