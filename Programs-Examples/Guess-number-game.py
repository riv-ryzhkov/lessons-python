import random


def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

            attempts += 1

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")


if __name__ == "__main__":
    guess_the_number()