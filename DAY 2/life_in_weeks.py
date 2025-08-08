# Don't change the code below
age = input("What is your current age")

year = 365
year1 = 52
year2 = 12
days_left = 90 - int(age) #assuming we were to live up to 90
x_days = days_left * year
y_weeks = days_left * year1
z_months = days_left * year2
print(f"you have {x_days} days, {y_weeks} weeks, and {z_months} months left")