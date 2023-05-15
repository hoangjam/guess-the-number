#Number Guessing Game Objectives:

from art import logo
import random

print(logo)

def random_number():
    random_num = random.randint(1,100)
    return random_num

def compare(guess, number):
    if guess > number:
        return "+"
    elif guess < number:
        return "-"
    else:
        return "="

guesses_left = 0
win = False

print("Welcome to Number Guesser!\n I'm thinking of a number between 1-100")
difficulty = input("What difficulty would you like to play on? easy/hard: ")

if difficulty == "easy":
    guesses_left = 10
    print(f"You have {guesses_left} guesses")
else:
    guesses_left = 5
    print(f"You have {guesses_left} guesses")

number = random_number()
print(number)

while not win:
    guess = int(input("Guess a number: "))
    if compare(guess, number) == "+":
        print("Too high!")
        guesses_left -= 1
    elif compare(guess, number) == "-":
        print("Too low!")
        guesses_left -= 1
    else:
        print(f"You got it! The number was {number}")
        win = True

    if guesses_left == 0:
        win = True
        print("You ran out of guesses! You lose.")