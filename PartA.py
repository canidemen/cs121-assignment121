
def tokenize(text_file_path):
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
