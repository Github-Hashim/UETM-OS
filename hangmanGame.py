"""
Software Construction and Development Lab no 2
Author: Muhammad Hashim
Dated: September 27, 2023
"""
import random  # Import the 'random' module for generating random words

def choose_word():
    # List of words for the game
    word_list = ["apple","banana","cherry","date","elderberry","fig","grape","honeydew","lemon"]

    # Return a randomly chosen word from the list
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    # Create a string to display the guessed and hidden letters of the word
    for letter in word:
        if letter in guessed_letters:
            display += letter  # Display guessed letters
        else:
            display += "_"
    return display


def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    print("Welcome to Hangman!")

    while True:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        # Check for valid input (single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)  # Add the guessed letter to the list

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        # Check if the word has been fully guessed
        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

        # Check if the player has used all attempts
        if attempts == 0:
            print("\nGame over! The word was:", word_to_guess)
            break
