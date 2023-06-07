import random
from enum import Enum


class State(Enum):
  active = 1
  inactive = 2

def get_choices():
  player_choice = input("Enter choice for rock paper sicssor: ")
  options = ["rock", "papers", "sicssors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player,computer):
    valueType = isinstance(player,str)
    if valueType == True:
      print(f"You Chose {player} ,Computer Chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
      if computer == "sicssors":
        return "You win!"
    elif player == "rock":
      if computer == "papers":
        return "tied!"
    elif player == "sicssors":
      if computer == "papers":
        return "You win!"
      else:
        return "you lost!"

choices= get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
print(State.active.value)
