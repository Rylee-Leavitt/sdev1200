#
# Rylee Leavitt
# 2/5/2025
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import random #imports the random module

def get_computer_choice(): #Defines the function get_computer_choice; no parameters are defined

    choices = ['rock', 'paper', 'scissors'] 
    # a list of choices for the computer to choose from

    return random.choice(choices) 
    # select a random choice from the list and returns it as the computer's choice.

def determine_winner(user_choice, computer_choice): 
    if user_choice == computer_choice: # Compares the user's choice and the computer's choice.
        # user_choice == computer_choice print its a tie
        return "It's a tie! Play again to determine the winner." 

        # if user_choice != computer_choice
        #if user_choice == 'rock' and computer_choice == 'scissors'
        #or user_choice == 'scissors' and computer_choice == 'paper' or
        #user_choice == 'paper' and computer_choice == 'rock'
        #return You win!
        # otherwise return You lose!

    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return f"You win! {user_choice.capitalize()} beats {computer_choice}."
    else:
        return f"You lose! {computer_choice.capitalize()} beats {user_choice}."

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = get_computer_choice()
        print(f"The computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "tie" not in result:
            break

if __name__ == "__main__":
    main()
