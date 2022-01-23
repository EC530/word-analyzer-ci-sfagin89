import nltk

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
            # for word in line.split():
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
        # print("Word: %s and count: %d" % x % histogram[x])

# load_histogram('test.txt')
# print_histogram()
