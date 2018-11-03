import unittest
import capitalize


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = capitalize.cap_text(text)
        self.assertEquals(result,'Python')

    def test_multiple_word(self):
        text = 'monty python'
        result = capitalize.cap_text(text)
        self.assertEquals(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()