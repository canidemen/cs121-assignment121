
def tokenize(text_file_path) -> list:
    """
    Runtime Complexity: O(N)

    Opens the file specified by the given file path and tokenizes valid inputs to a list.
    The function iterates through the file character by character to identify and collect
    alphanumeric characters (a-z, A-Z, 0-9).

     :param text_file_path: str
        A string representing the path to the text file.
    :return: List[str]
        A list of tokens extracted from the file.
    """
    tokens = []
    try:
        with open(text_file_path, 'r') as file:
            word = ""
            for line in file:
                for char in line:
                    order = ord(char)
                    if (47 < order < 58) or (64 < order < 91) or (96 < order < 123):
                        word += char
                    else:
                        if word:
                            tokens.append(word)
                        word = ""
    except FileNotFoundError:
        print(f"File not found: {text_file_path}")

    return tokens


def computeWordFrequencies(tokens: list[str]) -> dict:
    """
    Runtime Complexity: O(N)

    Computes the frequency of each word in the list of tokens.

    :param tokens: list[str]
        A list of tokens.
    :return: dict[str, int]
        A dictionary storing the word frequencies in the file.
    """

    tokens_dict = {}
    for i in tokens:
        try:
            if not isinstance(i, str):
                raise TypeError(f"Instance is of wrong type, {type(i)}")
        except TypeError as e:
            continue
        if i in tokens_dict:
            tokens_dict[i] += 1
        else:
            tokens_dict[i] = 1
    return tokens_dict


def print_tokens(frequencies: dict[str, int]) -> None:
    """
    Runtime Complexity: O(N)

    Prints the tokens and their frequencies in descending order of frequency and ascending order of token.

    :param frequencies: dict[str, int]
       A dictionary containing the frequencies of tokens.
    """

    sorted_dict = dict(sorted(frequencies.items(), key=lambda item: (-item[1], item[0])))
    for key, value in sorted_dict.items():
        print(key, " ", value)
