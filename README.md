# cs121-assignment1

This project consists of two Python scripts, PartA.py and PartB.py, designed for text processing and comparison.

## PartA.py

PartA.py contains functions for tokenizing text files and computing word frequencies.

- `tokenize(text_file_path)`: Opens the file specified by the given file path and tokenizes valid inputs to a list. The function iterates through the file character by character to identify and collect alphanumeric characters (a-z, A-Z, 0-9).
      The runtime complexity of this function is O(N), where N is the total number of characters in the file. 

- `computeWordFrequencies(tokens: list[str])`: Computes the frequency of each word in the list of tokens.
      The runtime complexity of this function is O(N), where N is the total number of tokens in the input list. 

- `print_tokens(frequencies: dict[str, int])`: Prints the tokens and their frequencies in descending order of frequency and ascending order of token.
      The overall time complexity of printing all tokens is O(N), where N is the number of unique tokens in the dictionary.

## PartB.py

PartB.py provides a function for comparing word frequencies between two text files.

- `tokenize_file(file_path)`: Tokenizes the content of the file specified by the given file path and computes the word frequencies.
      The overall time complexity of tokenize_file is O(N) as both the time complexities of PartA.tokenize() and PartA.computeWordFrequencies are O(N).

- `compare_files()`: Compares the word frequencies of two files and prints common words and their occurrences. 
      The time complexity of the function is O(N) (for tokenization and frequency computation) + O(M1) (for the nested loop). So, the time complexity for the compare_files function can indeed be simplified to O(N).

## Usage

To use these scripts:

1. Ensure Python is installed on your system.
2. Run `PartA.py` to tokenize text files and compute word frequencies.
3. Run `PartB.py` to compare word frequencies between two text files.