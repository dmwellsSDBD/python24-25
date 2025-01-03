'''
Guess the number game
'''
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
guess = None

print("Guess the secret number between 1 and 10")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print('Too Low!')
    elif guess > secret_number:
        print('Too High!')
    else:
        print('Congratulations! You are a winner!!')

print('Would you like to play again?')