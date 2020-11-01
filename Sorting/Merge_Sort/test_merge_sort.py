import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        arr = [3, 4, 1, 2, 5, 6]
        self.assertListEqual(merge_sort(arr), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
