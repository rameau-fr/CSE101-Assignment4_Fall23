def character_frequency(text, char):
    """
    Compute the frequency of a specific character in a given text using recursion.

    Args:
        text (str): The text in which to search for the character.
        char (str): The character whose frequency is to be calculated.

    Returns:
        int: The frequency of the character in the text.
    """
    # Student code starts here
    pass  # Replace 'pass' with your recursive function code

def separate_words(text, words, current_word=""):
    """
    Separate a string into words based on spaces, using recursion.

    Args:
        text (str): The text to be split into words.
        words (list): The list where separated words will be appended.
        current_word (str): The current word being formed (used in recursion).

    Returns:
        None: Modifies words in place.
    """
    # Student code starts here
    pass  # Replace 'pass' with your recursive function code


def word_frequency(words, word):
    """
    Compute the frequency of a specific word in a list of words using recursion.

    Args:
        words (list): List of words to search through.
        word (str): The word whose frequency is to be calculated.

    Returns:
        int: The frequency of the word in the list.
    """
    # Student code starts here
    pass  # Replace 'pass' with your recursive function code

def word_finder(words, query_word, index):
    """
    Find the index of a specific word in a list of words using recursion.

    Args:
        words (list): List of words to search through.
        query_word (str): The word to find.
        index (int): The current index in the list (used in recursion).

    Returns:
        int/bool: The index of the word if found, False otherwise.
    """
    # Student code starts here
    pass  # Replace 'pass' with your recursive function code

def unique_words(words, unique_words_list):
    """
    Extract unique words from a list of words using recursion.

    Args:
        words (list): List of words to process.
        unique_words_list (list): List where unique words will be appended.

    Returns:
        None: Modifies unique_words_list in place.
    """
    # Student code starts here
    pass  # Replace 'pass' with your recursive function code

def word_histogram(words, unique_words_list, histogram):
    """
    Create a histogram (frequency count) of words in a list using recursion.

    Args:
        words (list): List of words to analyze.
        unique_words_list (list): List of unique words.
        histogram (list): List where frequency counts will be appended.

    Returns:
        None: Modifies histogram in place.
    """
    # Student code starts here
    pass  # Replace 'pass' with your recursive function code

def main():
    
    text = "Science is built up of facts , as a house is with stones . \
        But a collection of facts is no more a science than a heap of \
        stones is a house ."
    
    # Exercise 1
    print(character_frequency(text, "e"))  # Expected output: 11
    
    # Exercise 2
    words_list = []
    separate_words(text, words_list)
    print(words_list)  # Expected output: ['Science', 'is', 'built', 'up', 'of', 'facts', ',', 'as', 'a', 'house', 'is', 'with', 'stones', '.', 'But', 'a', 'collection', 'of', 'facts', 'is', 'no', 'more', 'a', 'science', 'than', 'a', 'heap', 'of', 'stones', 'is', 'a', 'house', '.']

    # Exercise 3
    print(word_finder(words_list, "more", 0))  # Expected output: 21

    # Exercise 4
    unique_words_list = []
    unique_words(words_list, unique_words_list)
    print(unique_words_list)  # Expected output: ['Science', 'is', 'built', 'up', 'of', 'facts', ',', 'as', 'a', 'house', 'with', 'stones', '.', 'But', 'collection', 'no', 'more', 'science', 'than', 'heap']
    
    # Exercise 5
    frequency = word_frequency(words_list, "is")
    print(frequency)  # Expected output: 4
    
    # Exercise 6
    histogram = []
    word_histogram(words_list, unique_words_list, histogram)
    print(histogram)  # Expected output: [1, 4, 1, 1, 3, 2, 1, 1, 5, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1]

if __name__ == "__main__":
    main()
