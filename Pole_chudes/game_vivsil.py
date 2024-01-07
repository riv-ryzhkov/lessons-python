import random
# Let's create our code by explaining step by step. Read the code comments.
# Load the words file to your colab and then:
with open("words_alpha.txt") as f:
    words = [word.strip() for word in f.readlines()]

# create a function of the random library we downloaded using the random select function
def get_word():
    return random.choice(words)

# define a function related to the progress of the game
def show_state(word, guesses, wrong_guesses):
    # show the word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

    # show the wrong guesses
    if len(wrong_guesses) > 0:
        print("Wrong guesses: {}".format(" ".join(wrong_guesses)))

    # draw the hanged man
    print("")
    if len(wrong_guesses) >= 1:
        print("  0  ")
    if len(wrong_guesses) == 2:
        print("  |  ")
    elif len(wrong_guesses) == 3:
        print(" \|  ")
    elif len(wrong_guesses) >= 4:
        print(" \|/ ")
    if len(wrong_guesses) == 5:
        print(" /   ")
    elif len(wrong_guesses) >= 6:
        print(" / \ ")

# Create a function to play the game
def play():
    word = get_word()
    guesses = set()
    wrong_guesses = []
    max_wrong_guesses = 7

    while True:
        # Show the game
        show_state(word, guesses, wrong_guesses)

        # Get the player's guess
        guess = input("Write a letter: ").lower()

        # Check if the guess is a letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid! Please write just letter.")
            continue

        # Look if the letter has already been guessed
        if guess in guesses:
            print("Are you serious? Don't you remember you already guessed that letter.")
            continue

        # Add the guess to guesses
        guesses.add(guess)

        # Look if the guess is correct
        if guess in word:
            if set(word) == guesses:
                show_state(word, guesses, wrong_guesses)
                print("Finally, you win!")
                return
        else:
            wrong_guesses.append(guess)
            if len(wrong_guesses) == 4:
                print("You passed half of the way!")
            elif len(wrong_guesses) == 7:
                show_state(word, guesses, wrong_guesses)
                print("Last chance, use it carefully!")
            if len(wrong_guesses) >= max_wrong_guesses:
                show_state(word, guesses, wrong_guesses)
                print("You have no idea about this game, do you? The word was '{}'.".format(word))
                return

# Play the game
play()