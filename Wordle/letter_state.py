class LetterState:
    def __init__(self, character: str):
        # Initialize a LetterState object with a given character
        self.character: str = character

        # Initialize flags to track the state of the letter
        self.is_in_word: bool = False  # Flag to indicate if the letter is in the word
        self.is_in_position: bool = False  # Flag to indicate if the letter is in the correct position

    def __repr__(self):
        # Return a string representation of the LetterState object
        return f"[{self.character} is_in_word: {self.is_in_word} is_in_position: {self.is_in_position}]"