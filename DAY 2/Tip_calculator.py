print("welcome to the tip calculator!")
total_bill = input("what was the total bill? $")
percentage_tip= input("what percentage tip would you like to give? 10, 12, or 15? ")
people_split = input("How many people to split the bill? ")
total1_bill= round( float(total_bill) / int(people_split) * (1 + int(percentage_tip) / 100), 2)
#if the bill was $150.00, split between 5 people, with 12% tip.
#each person should pay (150.00 / 5) * 1.12
#round the result to 2 decimal places
total1_bill = "{:.2f}" . format(total1_bill)
#formatting adds the "0" behind the answer ---when answer is a 1 decimal place like "33.6"
print(f"Each person should pay: ${total1_bill} ")