def main():
    # Define the paths for input and output files
    input_file_path = "Wordle/word_source.txt"
    output_file_path = "Wordle/wordle_words.txt"

    # Create an empty list to store five-letter words
    five_letter_words = []

    # Open and read the input file
    with open(input_file_path, "r") as f:
        # Read each line from the file
        for line in f.readlines():
            word = line.strip()  # Remove leading/trailing whitespace
            if len(word) == 5:  # Check if the word has 5 letters
                five_letter_words.append(word)  # Add it to the list

    # Open and write to the output file
    with open(output_file_path, "w") as f:
        # Write each five-letter word to the output file
        for word in five_letter_words:
            f.write(word + "\n")  # Add a newline after each word

    # The 'pass' statement is not needed and can be removed

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()