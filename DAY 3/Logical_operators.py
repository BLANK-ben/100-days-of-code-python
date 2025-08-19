# "and, or, not"
print("welcome to the rollercoaster!")
height = int(input("wht is your height in cm?"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("You have a free ride!")    
#we can use as many elif's as we like        
    else:
        bill = 12
        print("Adult tickets are $12.")    
    wants_photo = input("do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
       bill += 3
      #Add $3 to their bill  
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")    