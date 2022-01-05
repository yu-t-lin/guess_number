
import random


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)



def start_game():
  if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
    return game(10)
  else:
    return game(5)

def game(counter):
  end_of_game = False
  while not end_of_game:
    while counter > 0:
      print(f"You have {counter} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == number:
        print("You got it right!")
        end_of_game = False
        if input(print("Did you want to play again? Type 'y' or 'n'.")) == 'y':
          start_game()
          counter = 0
        else:
          print("game_over")
          counter = 0
        
      elif guess > number:
        print("Too high.")
      elif guess < number:
        print("Too low.")
      
      counter -= 1
    if counter == 0:
      if input(print("You Lose! Did you want to play again? Type 'y' or 'n'.")) == 'y':
         start_game()
      else:
        print("game_over")
        end_of_game = False   

  # if end_of_game == False:   
  #   if input(print("Did you want to play again? Type 'y' or 'n'.")) == 'y':
  #     start_game()
  #   else:
  #     print("game_over")


start_game()







