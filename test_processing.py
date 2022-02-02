import histogram
import itertools

# Test file to check functionality of histogram script

input_list = [
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

# Expected result from testing process_content() function
expected_output = [
    "test",
    "histogram",
    "file",
    ",",
    "see",
    "reads",
    "words",
    "count",
    "occurrences",
    ".",
    "second",
    "occurrence",
    "word",
    "test",
    ",",
    "punctuation",
    "removal",
    "."
]


def test_processing():
    resulting_output = histogram.process_content(input_list)
    for (word1, word2) in zip(expected_output, resulting_output):
        assert word1 == word2
