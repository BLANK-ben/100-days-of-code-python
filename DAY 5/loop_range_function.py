# for loop with range
# for number in range(1, 11, 3): the range does not include the number 11
    #if we want number from 1-10 we do 1,11
    # the range function will step through the number in the bracket and increase it by 1
    #if we wanted it increase by any other number, we add another comma and the number we wanna increase with
    # print(number)

    #how do we add up num from 1-100 using code
total = 0
for number in range(1, 101):
        total += number
print(total)    