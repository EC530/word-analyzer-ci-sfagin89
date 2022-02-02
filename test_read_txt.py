import histogram
import itertools

# Test file to check functionality of histogram script


# Expected test file histogram results
expected_list = [
    "This",
    "is",
    "a",
    "test",
    "of",
    "the",
    "histogram",
    "file",
    ",",
    "to",
    "see",
    "if",
    "it",
    "reads",
    "in",
    "all",
    "words",
    "and",
    "can",
    "then",
    "count",
    "occurrences",
    ".",
    "this",
    "is",
    "the",
    "second",
    "occurrence",
    "of",
    "the",
    "word",
    "and",
    "a",
    "test",
    "of",
    ",",
    "punctuation",
    "removal",
    "."
]


def test_readtxt():
    output_list = histogram.read_txt('test.txt')
    for (word1, word2) in zip(expected_list, output_list):
        assert word1 == word2
