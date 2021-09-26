# game.py
import os
from dotenv import load_dotenv

load_dotenv()

PLAYER_NAME = os.getenv("Gabriel", default="Player One")
print("Welcome", PLAYER_NAME, "to my Rock-Paper-Scissors game...")
import random

# PROMPT USER FOR INPUT

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

#Code inspired by Jake Wexelblatt's posted on Slack

if user_choice.lower() not in options:
    print("User did not make a valid choice")
    print("Try again, selecting either 'rock', 'paper', or 'scissors'")
    quit()

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)

#Code inspired by Basil Bseiso's posted on Slack

if(user_choice.lower() == "rock" and computer_choice == "scissors"):
    print("Congratulations, you win")
elif(user_choice.lower() == "rock" and computer_choice == "paper"):
    print("Oh, the computer won. Try again")
elif(user_choice.lower() == "paper" and computer_choice == "scissors"):
    print("Oh, the computer won. Try again")
elif(user_choice.lower() == "paper" and computer_choice == "rock"):
    print("Congratulations, you win")
elif(user_choice.lower() == "scissors" and computer_choice == "paper"):
    print("Congratulations, you win")
elif(user_choice.lower() == "scissors" and computer_choice == "rock"):
    print("Oh, the computer won. Try again")
else: print("It's a tie!")


print("THANKS PLEASE PLAY AGAIN")
