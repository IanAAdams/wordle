from math import remainder
from letter_state import LetterState

class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    VOIDED_LETTER = "*"

    def __init__(self, secret: str):
        # Initialize the Wordle game with a secret word.
        self.secret: str = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        # Record a player's attempt.
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        # Check a player's guess and return the result.
        word = word.upper()

        # Initialize the results array with all GREY letters.
        result = [LetterState(x) for x in word]

        # Make a copy of the secret so we can cross out 'used' letters.
        remaining_secret = list(self.secret)

        # First, check for GREEN letters.
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.is_in_position = True
                remaining_secret[i] = self.VOIDED_LETTER

        # Loop again and check for YELLOW letters.
        for i in range(self.WORD_LENGTH):
            letter = result[i]

            # Skip this letter if it is already in the right place.
            if letter.is_in_position:
                continue

            # Otherwise, check if the letter is in the word, and void that index.
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = self.VOIDED_LETTER
                    letter.is_in_word = True
                    break

        return result

    @property
    def is_solved(self):
        # Check if the game is solved by comparing the latest attempt with the secret.
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        # Calculate the number of remaining attempts.
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        # Check if the player can still make attempts.
        return self.remaining_attempts > 0 and not self.is_solved
