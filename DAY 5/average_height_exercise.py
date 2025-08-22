# Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# Don't change the code above

total_height = 0      
num_students = 0 

for height in student_heights:
    total_height += height   # add this student's height to the total
    num_students += 1        # count this student

average = total_height / num_students
print(f"Average height (rounded): {round(average)}")