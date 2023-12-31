#Number Guessing Game Objectives:
from art import logo
from random import randint

# Include an ASCII art logo.
print(logo)
print("Welcome to the Number Guessing Game!")
difficulty = input("Choose difficulty: Easy (e), Medium (m), or Hard (h): ").lower()

guess_remaining = 0

if difficulty == "e":
  guess_remaining = 10
elif difficulty == "m":
  guess_remaining = 7
elif difficulty == "h":
  guess_remaining = 5

print(f"You have {guess_remaining} guesses in this level")
# Allow the player to submit a guess for a number between 1 and 100.
correct_answer = randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
while guess != correct_answer or guess_remaining > 0:
  if guess > correct_answer:
    print("Too high.")
    print(f"You have {guess_remaining} guesses remaining.")
    guess = int(input("Pick a smaller number: "))
    guess_remaining -= 1
    
  elif guess < correct_answer:
    print("Too low.")
    print(f"You have {guess_remaining} guesses remaining.")
    guess = int(input("Pick a larger number: "))
    guess_remaining -= 1
    
  elif guess == correct_answer:
    print(f"You guessed it! With {guess_remaining} guesses left")
    break
    
  if guess_remaining == 0 and guess != correct_answer:
    print(f"You ran out of guesses. You Lose. The correct answer was {correct_answer}.")
    break
