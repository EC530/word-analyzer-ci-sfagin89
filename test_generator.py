import histogram
import itertools

# Test file to check functionality of histogram script

input_list = [
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

# Expected result from testing generate_histogram() function
expected_output = {
"test": 2,
"histogram": 1,
"file": 1,
",": 2,
"see": 1,
"reads": 1,
"words": 1,
"count": 1,
"occurrences": 1,
".": 2,
"second": 1,
"occurrence": 1,
"word": 1,
"punctuation": 1,
"removal": 1
}

def test_generator():
    resulting_output = histogram.generate_histogram(input_list)
    for (key1, key2) in zip(expected_output, resulting_output):
        assert key1 == key2 and expected_output[key1] == resulting_output[key2]
