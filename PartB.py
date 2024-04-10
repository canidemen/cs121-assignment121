import PartA
import sys      #for sys.argv[]

def tokenize_file(file_path):
    """
       Tokenizes the content of the file specified by the given file path and computes the word frequencies.

       :param file_path: str
           A string representing the path to the file.
       :return: dict[str, int]
           A dictionary storing the word frequencies in the file.
    """

    file_list = PartA.tokenize(file_path)
    return PartA.computeWordFrequencies(file_list)


def compare_files():
    """
       Compares the word frequencies of two files and prints common words and their occurrences.

       This function takes two file paths from command-line arguments, tokenizes each file, computes
       word frequencies, and then compares the frequencies to identify common words.

    """

    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    file_1_dict = tokenize_file(file_1)
    file_2_dict = tokenize_file(file_2)
    similar_words = []

    for token in file_1_dict:
        if token in file_2_dict:
            if token in similar_words:
                continue
            else:
                similar_words.append(token)

    print(f"Common words:")
    for i in similar_words:
        print(i)

    print(f"\nCommon occurrences:\n{len(similar_words)}")


if __name__ == "__main__":
    compare_files()
