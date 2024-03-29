
import random

from art import logo

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5 



def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! the answer was {answer}.")



def difficulty():
  level = input("Choose a difficulty. Type 'easy or 'hard'. ")
  global turns
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS 

def game():

  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)

  turns = difficulty()


  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")  
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print("Game over")
      return
    elif guess != answer:
      print("Guess again.")



game()   








