is_leap = input(f"Is it leap year or not? (yes/no) : ")
if is_leap == 'yes':
    year = 366
    
elif is_leap == 'no':
    year = 365
else :
    print(f"You have to either say 'yes' or 'no' ")
    exit()
hour = 24*year
minute = 60*hour
second= 60* minute

print(f"There are {second} seconds in that year")
    