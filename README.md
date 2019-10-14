# DNAencoder

Python program to encode/decode DNA and RNA

## Description:

This program runs a series of test cases to test the following objectives:
- Provides mechanism to encode ASCII text string as DNA/RNA assuming they are valid string
- Provides mechanism to decode DNA and output ASCII equivalent
- Provides interface to identify substring as DNA
- Provides interface to identify longest common subsequence

## Installation:

Relevant dependencies are included in the conda package:
```bash
pip install conda
```

## Usage:

To run the program and the included testcases ensure you are in the correct directory and use the command:
```bash
python encoder.py
```

## Testing:

I used the unittest framework to write testcases for my program. In order to make additions to the test cases follow this template:

```python
    def test_nameoftest(self): #'nameoftest' can be changed to chosen name for testcase
        actual = main('expectedinputgoeshere')  #'expectedinputgoeshere' can be changed to any string input you wish to test
        expected = 'expectedoutputgoeshere'   #'expectedoutputgoeshere' can be changes to expected output corresponding to expected input
        self.assertEqual(actual, expected)
```
Once the addition is made to the test class, run the program to run all test cases. If test returns 'OK' test case has passed else it will display the difference to expected or error it has run into.

