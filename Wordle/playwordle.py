from typing import List
from letter_state import LetterState
from wordle import Wordle
from colorama import Fore
import random


def main():
    # Load a set of words from a file
    word_set = load_word_set("Wordle/wordle_words.txt")
    
    # Choose a random secret word from the loaded word set
    secret = random.choice(list(word_set))
    
    # Create a Wordle game instance with the secret word
    wordle = Wordle(secret)

    # Keep running the game as long as the player has attempts left
    while wordle.can_attempt:
        x = input("\nType your guess: ").upper()

        # Check if the input word has the correct length
        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word must be {wordle.WORD_LENGTH} characters long!"
                + Fore.RESET
            )
            continue

        # Check if the input word is a valid word in the word set
        if not x in word_set:
            print(
                Fore.RED
                + f"{x} is not a valid word!"
                + Fore.RESET
            )
            continue

        # Attempt to guess the word and update the game state
        wordle.attempt(x)
        
        # Display the game results after each attempt
        display_results(wordle)

    # Check if the player solved the puzzle or failed
    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")
        print(f"The secret word was: {wordle.secret}")

def display_results(wordle: Wordle):
    # Print the header for displaying results
    print("\nYour results so far...")
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []  # Initialize a list to store lines of results

    # Display the player's previous attempts and results
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    # Fill in remaining attempts with underscores
    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    # Draw a border around the results
    draw_border_around(lines)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()  # Read each line, strip whitespace, and convert to uppercase
            word_set.add(word)  # Add the word to the word_set
    return word_set  # Return the set of words

def convert_result_to_color(result: List[LetterState]):
    result_with_color = []  # Initialize a list to store colored results
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN  # Set color to green for correct position
        elif letter.is_in_word:
            color = Fore.YELLOW  # Set color to yellow for correct letter in the word
        else:
            color = Fore.WHITE  # Set color to white for other cases
        colored_letter = color + letter.character + Fore.RESET  # Apply color to the letter
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)  # Join colored letters into a single string

def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"  # Create the top border
    bottom_border = "└" + "─" * content_length + "┘"  # Create the bottom border
    space = " " * pad
    print(top_border)  # Print the top border

    # Print each line with borders
    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)  # Print the bottom border

if __name__ == "__main__":
    main()  # Start the main function if this script is executed
