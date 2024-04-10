# cs121-assignment1

This project consists of two Python scripts, PartA.py and PartB.py, designed for text processing and comparison.

## PartA.py

PartA.py contains functions for tokenizing text files and computing word frequencies.

- `tokenize(text_file_path)`: Opens the file specified by the given file path and tokenizes valid inputs to a list. The function iterates through the file character by character to identify and collect alphanumeric characters (a-z, A-Z, 0-9).

- `computeWordFrequencies(tokens: list[str])`: Computes the frequency of each word in the list of tokens.

- `print_tokens(frequencies: dict[str, int])`: Prints the tokens and their frequencies in descending order of frequency and ascending order of token.

## PartB.py

PartB.py provides a function for comparing word frequencies between two text files.

- `tokenize_file(file_path)`: Tokenizes the content of the file specified by the given file path and computes the word frequencies.

- `compare_files()`: Compares the word frequencies of two files and prints common words and their occurrences.

    This function takes two file paths as command-line arguments, tokenizes each file, computes word frequencies, and then compares the frequencies to identify common words.

## Usage

To use these scripts:

1. Ensure Python is installed on your system.
2. Run `PartA.py` to tokenize text files and compute word frequencies.
3. Run `PartB.py` to compare word frequencies between two text files.