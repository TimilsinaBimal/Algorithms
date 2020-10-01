import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        data = [1, 2, 3, 5, 6, 7, 8]
        self.assertEqual(binary_search(data, 0, len(data)-1, 5), 3)
        self.assertEqual(binary_search(data, 0, len(data)-1, 10), -1)

    def test_searchChar(self):
        data = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(binary_search(data, 0, len(data)-1, 'a'), 0)
        self.assertEqual(binary_search(data, 0, len(data)-1, 'f'), -1)


if __name__ == "__main__":
    unittest.main()
