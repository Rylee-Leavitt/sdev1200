#
# Rylee Leavitt
# 2/21/25
# Trivia Game Programming Project
# SDEV 1200
#

# # main.py

from questions import Question, questions

def play_game():
    player1_score = 0
    player2_score = 0

    print("Player 1's turn:")
    for i in range(5):
        question = questions[i]
        print(f"Q{i+1}) {question.get_question()}")
        print(f"1.) {question.get_ans1()}")
        print(f"2.) {question.get_ans2()}")
        print(f"3.) {question.get_ans3()}")
        print(f"4.) {question.get_ans4()}")
        answer = int(input("Your answer: "))
        if answer == question.get_correct_ans():
            player1_score += 1

    print("Player 2's turn:")
    for i in range(5, 10):
        question = questions[i]
        print(f"Q{i-4}: {question.get_question()}")
        print(f"1: {question.get_ans1()}")
        print(f"2: {question.get_ans2()}")
        print(f"3: {question.get_ans3()}")
        print(f"4: {question.get_ans4()}")
        answer = int(input("Your answer: "))
        if answer == question.get_correct_ans():
            player2_score += 1

    print(f"Player 1 scored: {player1_score}")
    print(f"Player 2 scored: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Start the game
play_game()
