name = input(f"Enter your name : ")
date = input(f"Enter your Date of Birth : ")
mob_no = input(f"Enter your telephone number : ")
email = input(f"Enter your email address : ")
address = input(f"Enter your home address : ")

person = {"Name": name, "Date Of Birth":date, "Telephone number" : mob_no, "Email Address": email,"Home Address": address}
print("-"*50, end = "")
print()
print(f"Here is your contact card\n\n")
for key,value in person.items():
    print(f"{key} : {value}")