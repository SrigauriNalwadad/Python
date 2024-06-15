import random as r
from art import logo

print(logo)
print("\nWelcome to Guessing the Number Game!")
print("\nI'm thinking of a number from 1 to 100")
difficulty_level = (input("Choose a diffculty level. Type 'easy' or 'hard': ")).lower()

number = r.randint(1,101)
print(number)

if difficulty_level == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    for num in range(0,6):
        if guessed_number != number:
            attempts = attempts - 1
            print(f"You have {attempts} attempts remaining to guess the number.")

elif difficulty_level == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempts = attempts - 1

else:
    print("You have undifined attempts remaining to guess the number.")