import numbers
import re
import random

# Get the answer
pool_file = open("hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line :
    pool_answers.append(pool_answer_line)

    pool_answer_line = pool_file.readline()
answer = random.choice(pool_answers)

answer = answer.upper()

#Pre-game set up.
answer_guesssed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guesssed.append(False)
    else:
        answer_guesssed.append(True)

# Game logic.
num_of_incorrect_guesses = 5

current_incorrect_guesses = 0

letters_guessed = []

# let user play the game.
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guesssed:
    #display game status
    print(f"Number of incorrect guesses remaining: "[num_of_incorrect_guesses - current_incorrect_guesses])