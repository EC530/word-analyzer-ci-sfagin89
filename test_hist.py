import histogram
import itertools

# Test file to check functionality of histogram script


# Expected test file histogram results
expected_hist = {
"this": 2,
"is": 2,
"a": 2,
"test": 2,
"of": 3,
"the": 3,
"histogram": 1,
"file": 1,
",": 2,
"to": 1,
"see": 1,
"if": 1,
"it": 1,
"reads": 1,
"in": 1,
"all": 1,
"words": 1,
"and": 2,
"can": 1,
"then": 1,
"count": 1,
"occurrences": 1,
".": 2,
"second": 1,
"occurrence": 1,
"word": 1,
"punctuation": 1,
"removal": 1
}

def test_histogram():
    histogram.load_histogram('test.txt')
    for (key1, key2) in zip(expected_hist, histogram.histogram):
        assert key1 == key2 and expected_hist[key1] == histogram.histogram[key2]
