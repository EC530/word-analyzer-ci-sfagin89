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


def test_display(capfd):
    histogram.display_histogram(input_dict)
    output, err = capfd.readouterr()
    assert output == "[test] occurs 2 times in the text.\n[histogram] occurs 1 times in the text.\n[file] occurs 1 times in the text.\n[,] occurs 2 times in the text.\n[see] occurs 1 times in the text.\n[reads] occurs 1 times in the text.\n[words] occurs 1 times in the text.\n[count] occurs 1 times in the text.\n[occurrences] occurs 1 times in the text.\n[.] occurs 2 times in the text.\n[second] occurs 1 times in the text.\n[occurrence] occurs 1 times in the text.\n[word] occurs 1 times in the text.\n[punctuation] occurs 1 times in the text.\n[removal] occurs 1 times in the text."
