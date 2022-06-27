
import os
import unittest

from cdfutils import Textfile


TEST_FILENAME = os.path.join(os.path.dirname(__file__), 
                             r"testQuotes.txt")

class TestConfig(unittest.TestCase):

    def test_RandomSection(self):
        with open(TEST_FILENAME) as f:
            wholeFile = f.read()
            self.assertTrue(Textfile.RandomSection(f) in wholeFile)

    def test_RandomLine(self):
        with open(TEST_FILENAME) as f:
            wholeFile = f.read()
            self.assertTrue(Textfile.RandomLine(f) in wholeFile)

if __name__ == "__main__":
    unittest.main()
