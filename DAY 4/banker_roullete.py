import random
 # Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# Don't change the code above 

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_paying = names[random_choice]
print(person_paying + " is going to buy the meal today")