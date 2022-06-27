
import os
import unittest

from cdfutils import Textfile


TEST_FILENAME = r"testQuotes.txt"

class TestConfig(unittest.TestCase):

    def test_randomSection(self):
        with open(TEST_FILENAME) as f:
            wholeFile = f.read()
            self.assertTrue(Textfile.randomSection(f) in wholeFile)

    def test_randomLine(self):
        with open(TEST_FILENAME) as f:
            wholeFile = f.read()
            self.assertTrue(Textfile.randomLine(f) in wholeFile)

if __name__ == "__main__":
    unittest.main()
