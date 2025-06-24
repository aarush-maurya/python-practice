# 8: Generation Classifier
print("\033[32m=== Generation Classifier ===\033[0m")
ans = input("Do you know your 'age' or 'year' of birth? ").lower()
while ans not in ["age", "year"]:
    ans = input("Please enter either 'age' or 'year': ")
if ans == "age":
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Generation Alpha")
    elif age <= 28:
        print("Generation Z")
    elif age <= 44:
        print("Millennial")
    elif age <= 60:
        print("Gen X")
    elif age <= 79:
        print("Baby Boomer")
    elif age <= 96:
        print("Silent Generation")
    else:
        print("Greatest or Lost Generation")
elif ans == "year":
    year = int(input("Enter your birth year: "))
    if year >= 2013:
        print("Generation Alpha")
    elif year >= 1997:
        print("Generation Z")
    elif year >= 1981:
        print("Millennial")
    elif year >= 1965:
        print("Gen X")
    elif year >= 1946:
        print("Baby Boomer")
    elif year >= 1928:
        print("Silent Generation")
    else:
        print("Greatest or Lost Generation")