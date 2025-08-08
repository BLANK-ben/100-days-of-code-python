# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height) ** 2
BMI = int(weight) / new_height
print(BMI)