import unittest
from Homework_4 import character_frequency, separate_words, word_frequency, word_finder, unique_words, word_histogram

class TestHomework4(unittest.TestCase):
    
    def test_character_frequency(self):
        self.assertEqual(character_frequency("hello world", "l"), 3)
        self.assertEqual(character_frequency("test", "t"), 2)
        #self.assertEqual(character_frequency("", "a"), 0)

    def test_separate_words(self):
        words_list = []
        separate_words("hello world from python", words_list)
        self.assertEqual(words_list, ["hello", "world", "from", "python"])
        words_list.clear()
        separate_words("goodbye cruel world", words_list)
        self.assertEqual(words_list, ["goodbye", "cruel", "world"])

    def test_word_frequency(self):
        words = ["apple", "banana", "apple", "pear"]
        self.assertEqual(word_frequency(words, "apple"), 2)
        self.assertEqual(word_frequency(words, "banana"), 1)
        self.assertEqual(word_frequency(words, ""), 0)

    def test_word_finder(self):
        words = ["apple", "banana", "pear"]
        self.assertEqual(word_finder(words, "banana", 0), 1)
        self.assertEqual(word_finder(words, "pear", 0), 2)
        self.assertEqual(word_finder(words, "cherry", 0), False)

    def test_unique_words(self):
        words = ["apple", "banana", "apple", "pear"]
        unique_words_list = []
        unique_words(words, unique_words_list)
        self.assertEqual(unique_words_list, ["apple", "banana", "pear"])
        unique_words_list.clear()
        unique_words(["cherry", "cherry", "cherry"], unique_words_list)
        self.assertEqual(unique_words_list, ["cherry"])

    def test_word_histogram(self):
        words = ["apple", "banana", "apple", "pear", "banana"]
        unique_words_list = ["apple", "banana", "pear"]
        histogram = []
        word_histogram(words, unique_words_list, histogram)
        self.assertEqual(histogram, [2, 2, 1])

if __name__ == '__main__':
    unittest.main()

"""
by Francois
.______     ______     ______    __  ___ 
|   _  \   /  __  \   /  __  \  |  |/  / 
|  |_)  | |  |  |  | |  |  |  | |  '  /  
|   _  <  |  |  |  | |  |  |  | |    <   
|  |_)  | |  `--'  | |  `--'  | |  .  \  
|______/   \______/   \______/  |__|\__\ 
                                         
"""
