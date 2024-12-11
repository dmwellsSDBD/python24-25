import random

def print_treasure_map():
    """Prints an ASCII treasure map."""
    print("""
         _______
        |       |
        |   X   |  <-- Treasure
        |_______|
    """)

def play_game():
    print("Welcome to the ASCII Treasure Hunt!")
    print_treasure_map()
    print("The treasure is hidden behind a number between 1 and 100.")

    treasure_number = random.randint(1, 100)
    attempts = 7  # Limit the number of attempts

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess == treasure_number:
                print("""
                Congratulations! You found the treasure!

                |  |  
               / \(\
              /   `-' \  <-- Treasure Chest
             /__________\
              \________/
                
                """)
                break

            elif guess < treasure_number:
                print("The treasure is deeper. Guess higher!")
            else:
                print("The treasure is higher up. Guess lower!")

            attempts -= 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == 0:
        print("\nGame over! You've run out of attempts.")
        print(f"The treasure was behind number {treasure_number}.")
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()