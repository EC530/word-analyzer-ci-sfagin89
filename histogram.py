import nltk
import pandas as pd
import matplotlib.pyplot as plt

# histogram.py
# 1/20/22
# sara fagin
#
# Creates a dictionary to hold both a word and the number of times that word
# has occured in the text being read. Each occurance of the word increments
# the value of that item in the dictionary.
#
# Implemented:
# Reads in a text file word by word, adding new words to the created histogram
# dictionary, and incrementing value of existing dictionary keys.
# Prints all the keys in the dictionary along with the number of occurances of
# that key.
#
# To Be Implemented:
# Currenty is case sensitive, change to case-insensitive
# Display the histogram.
#
# To Run:
# Option 1: Directly from python CLI (requires use of Python3)
# python3
# >>> import histogram
# >>> histogram.load_histogram('<file.txt>')
# >>> histogram.print_histogram()
# >>> exit()
# Option 2: Import to another Python file

# https://www.kite.com/python/answers/how-to-remove-all-punctuation-marks-with-nltk-in-python
# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
# https://www.nltk.org/_modules/nltk/tokenize/punkt.html
# https://realpython.com/python-histograms/


# Creating empty dictionary for histogram
# Example of future content {"word1: 24"}, word1 occurs 24 times in text.
histogram = {}
nltk.download('punkt')


def load_histogram(filename):
    with open(filename, 'r') as file:
        for line in file:
            sentence = nltk.word_tokenize(line)
            for word in sentence:
                word_lc = word.lower()
                if word_lc in histogram:
                    print("word is already present, increasing count")
                    count = histogram[word_lc]
                    histogram[word_lc] = count + 1
                else:
                    print("Adding word to histogram")
                    histogram[word_lc] = 1


def print_histogram():
    for x in histogram:
        print("[%s]" % x, "occurs %d times in the text." % histogram[x])


def graph_histogram():
    hist_data = pd.Series(data=histogram)
    hist_data.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
    plt.title('Number of Occurances of Unique Words')
    # plt.xlable('Occurances')
    # plt.ylable('Words')
    plt.grid(axis='y', alpha=0.75)
    # Commenting out Show, causes error with current Raspbian Release
    # plt.show()


def test_histogram():
    load_histogram('test.txt')
    print_histogram()
    # graph_histogram()
