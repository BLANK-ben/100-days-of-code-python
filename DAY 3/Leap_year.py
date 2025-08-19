#Don't change the code below 
year = int(input("Which year do you want to check?"))
#Don't change the code above

if year % 400 == 0:       # Rule 3: divisible by 400 → leap year
    print("leap year")
elif year % 100 == 0:     # Rule 2: divisible by 100 → not a leap year
    print("not a leap year")
elif year % 4 == 0:       # Rule 1: divisible by 4 → leap year
    print("leap year")
else:                     # Otherwise → not a leap year
    print("not a leap year")
