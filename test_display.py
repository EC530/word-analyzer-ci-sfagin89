import histogram
import itertools

# Test file to check functionality of histogram script


# Expected test file histogram results
input_dict = {
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

expected_output = [
"[test] occurs 2 times in the text.",
"[histogram] occurs 1 times in the text.",
"[file] occurs 1 times in the text.",
"[,] occurs 2 times in the text.",
"[see] occurs 1 times in the text.",
"[reads] occurs 1 times in the text.",
"[words] occurs 1 times in the text.",
"[count] occurs 1 times in the text.",
"[occurrences] occurs 1 times in the text.",
"[.] occurs 2 times in the text.",
"[second] occurs 1 times in the text.",
"[occurrence] occurs 1 times in the text.",
"[word] occurs 1 times in the text.",
"[punctuation] occurs 1 times in the text.",
"[removal] occurs 1 times in the text."
]


def test_display(capfd):
    histogram.display_histogram(input_dict)
    output, err = capfd.readouterr()
    for (line1, line2) in zip(output, expected_output):
        assert line1 == line2
