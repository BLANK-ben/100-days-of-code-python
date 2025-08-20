import random

# ASCII art for each choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store them in a list
choices = [rock, paper, scissors]

# Player input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

# Check for invalid input
if user_choice < 0 or user_choice >= 3:
    print("❌ Invalid choice, you lose!")
else:
    # Print the player's choice image
    print("You chose:")
    print(choices[user_choice])

    # Computer random choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
