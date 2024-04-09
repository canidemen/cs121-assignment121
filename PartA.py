import re

def tokenize(text_file_path):
    tokens = []
    regex = r'\w+'
    try:
        with open(text_file_path, 'r') as file:
            for line in file:
                tokens.extend(re.findall(regex, line.lower()))
    except FileNotFoundError:
        print(f"File not found: {text_file_path}")
        return []

    return tokens



def computeWordFrequencies(tokens: list[str]):
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


def print_tokens(frequencies: dict[str, int]):
    sorted_dict = dict(sorted(frequencies.items(), key=lambda item: (-item[1], item[0])))
    for key, value in sorted_dict.items():
        print(key, " ", value)
