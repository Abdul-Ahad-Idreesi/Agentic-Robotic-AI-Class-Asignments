
import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I have generated a random number between 1 and 100.")

    max_tries = 10
    tries_left = max_tries

    while tries_left > 0:
        try:
            guess = int(input(f"Enter your guess ({tries_left} tries left): "))
            if guess == secret_number:
                print("Excellent Guess")
                break
            else:
                tries_left -= 1
                print("TRY Again")
                if guess > secret_number:
                    print("Your Guess is too high")
                else:
                    print("Your Guess is too low")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    if tries_left == 0:
        print(f"You've run out of tries! The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()