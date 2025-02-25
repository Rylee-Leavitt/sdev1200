#
# Rylee Leavitt
# 2/21/25
# Trivia Game Programming Project
# SDEV 1200
#

# # main.py

from questions import Question, questions

def play_game():
    #Function that allows two players to answer 5 questions each and determines the winner based on the scores.

    player1_score = 0 #initializes Player 1's Score
    player2_score = 0 #initializes Player 's Score

    print("Player 1's turn:")   #Prints "Player 1's turn:
    for i in range(5):          #Sets the range of questions asked to five
        question = questions[i] #Changes the question with each iteration of the loop

        print(f"Q{i+1}) {question.get_question()}") #The trivia question is embedded
        #i+1 makes the question number start from 1 instead of 0

        print(f"1.) {question.get_ans1()}") #gets answer Choice #1
        print(f"2.) {question.get_ans2()}") #gets answer Choice #2
        print(f"3.) {question.get_ans3()}") #gets answer Choice #3
        print(f"4.) {question.get_ans4()}") #gets answer Choice #4

        answer = int(input("Your answer: ")) #asks the user for their input
        if answer == question.get_correct_ans(): #determines if the players input is the same as the answer
            player1_score += 1 #if input == answer, Player 1 gets a point

    print("Player 2's turn:")   #prints "Player 2's turn:
    for i in range(5, 10):      #Sets the range of questions asked to 10
        question = questions[i] #Changes the question with each iteration of the loop

        print(f"Q{i-4}: {question.get_question()}")

        print(f"1: {question.get_ans1()}") #gets answer Choice #1
        print(f"2: {question.get_ans2()}") #gets answer Choice #2
        print(f"3: {question.get_ans3()}") #gets answer Choice #3
        print(f"4: {question.get_ans4()}") #gets answer Choice #4

        answer = int(input("Your answer: ")) #asks the user for their input
        if answer == question.get_correct_ans(): #determines if the players input is the same as the answer
            player2_score += 1 #if input == answer Player 2, gets a point

    print(f"Player 1 scored: {player1_score}") #Prints Player 1's Score
    print(f"Player 2 scored: {player2_score}") #Prints Player 2's Score

    if player1_score > player2_score: #Determines if Player 1's Score is greater than Player 2's Score
        print("Player 1 wins!") #if so, Prints "Player 1 wins"

    elif player2_score > player1_score: #Determines if Player 1's Score is less than Player 2's Score
        print("Player 2 wins!") #if so, Prints "Player 2 wins"

    else:
        print("It's a tie!") #if neither condition is met, Prints "it's a tie"

# Start the game
play_game()
