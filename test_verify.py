import histogram

# Test file to check functionality of verify_file() function in histogram script


# Expected result from testing verify_file() function
expected_output1 = "txt"
expected_output2 = "Sorry that is an unsupported file type"


def test_verify():
    output1 = histogram.verify_file('test.txt')
    output2 = histogram.verify_file('test.html')
    assert output1 == expected_output1 and output2 == expected_output2
