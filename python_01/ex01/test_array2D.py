import unittest
from array2D import slice_me


class TestSliceMe(unittest.TestCase):

    def test_normal_slice(self):
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        result = slice_me(family, 0, 2)
        self.assertEqual(result, [[1.80, 78.4], [2.15, 102.7]])

    def test_negative_index_slice(self):
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        result = slice_me(family, 1, -2)
        self.assertEqual(result, [[2.15, 102.7]])

    def test_full_slice(self):
        family = [[1, 2], [3, 4], [5, 6]]
        result = slice_me(family, 0, 3)
        self.assertEqual(result, family)

    def test_empty_result_slice(self):
        family = [[1, 2], [3, 4], [5, 6]]
        result = slice_me(family, 2, 1)
        self.assertEqual(result, [])

    def test_row_size_mismatch(self):
        family = [[1, 2], [1, 2, 3]]
        with self.assertRaises(Exception):
            slice_me(family, 0, 1)

    def test_not_a_list(self):
        with self.assertRaises(Exception):
            slice_me("not a list", 0, 1)

    def test_empty_family(self):
        with self.assertRaises(Exception):
            slice_me([], 0, 1)

    def test_rows_not_lists(self):
        family = [1, 2, 3]
        with self.assertRaises(Exception):
            slice_me(family, 0, 1)

    def test_invalid_start_type(self):
        family = [[1, 2], [3, 4]]
        with self.assertRaises(Exception):
            slice_me(family, "0", 1)

    def test_invalid_end_type(self):
        family = [[1, 2], [3, 4]]
        with self.assertRaises(Exception):
            slice_me(family, 0, "1")

    def test_bool_as_start(self):
        family = [[1, 2], [3, 4]]
        with self.assertRaises(Exception):
            slice_me(family, True, 1)


if __name__ == "__main__":
    unittest.main()