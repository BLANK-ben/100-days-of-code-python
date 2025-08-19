print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
choice1 = input('go find the treasure."left" or "right"?').lower()

if choice1 == "left":
    choice2 = input('you\'re at a lake. an island is in the middle of the lake. Type "wait" to wait for a boat, Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("There is a house with 3 doors. one red, one yellow and one blue. which colour do you choose?\n").lower()
        if choice3 == "red":
            print("you were burnt alive.Game Over.")
        elif choice3 == "yellow":
            print("you found the treasure! You win!")
        elif choice3 == "blue":
            print("you were eaten alive. Game Over.")
    else:
        print("Game Over")        
else:
    print("Game over")                     