import recursion_challenge as rec
import unittest 

class TestStringMethods(unittest.TestCase):

    def test_flatten(self):
        flat = rec.flatten([[1, 2], [3, 4]])
        self.assertEqual(flat, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
