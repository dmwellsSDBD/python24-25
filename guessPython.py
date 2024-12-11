import random

def guessingGame():
    # Generate a random number between 1 and 100
    secretNumber = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Prompt the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100")
            elif guess < secretNumber:
                print("Your guess is too low. Try again.")
            elif guess > secretNumber:
                print("Your guess is too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.") 
            
if __name__ == "__main__":
    guessingGame()