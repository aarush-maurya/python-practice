print(f"\033[32m===Bill Separator===\033[0m")
bill_amount= float(input(f"Enter the Bill amount : "))
number_of_people = int(input(f"How many people are there? :"))
tip_verify = input(f"Do you also want to give tip? (yes/no): ")
tip = 0
if tip_verify == "yes":
    tip = float(input(f"Enter the percentage of bill that should be the tip : "))
    
elif tip_verify == "no":
    print(f"No tip, No problem.")
else:
    print(f"You either have to say 'yes or 'no")
tip_ = (tip/100)*bill_amount 
print(f"Each one of you has to pay {round((bill_amount/number_of_people), 2) }")
print(f"You have to give {tip_} as tip")
print(f"So you owe a total of {tip_ + bill_amount}")

