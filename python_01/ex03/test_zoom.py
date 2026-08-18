import unittest
import numpy as np
from zoom import zoom_me


class TestZoomMe(unittest.TestCase):
    """Independent tests for zoom_me. No dependency on load_image.py:
    a synthetic array is used instead of a real loaded image."""

    def setUp(self):
        # Deterministic 10x10x3 array to check the crop values precisely.
        self.small_array = np.arange(10 * 10 * 3).reshape(10, 10, 3)

    def test_returns_ndarray(self):
        result = zoom_me(self.small_array, 4)
        self.assertIsInstance(result, np.ndarray)

    def test_correct_shape(self):
        result = zoom_me(self.small_array, 4)
        self.assertEqual(result.shape, (4, 4, 1))

    def test_keeps_single_channel(self):
        result = zoom_me(self.small_array, 4)
        expected = self.small_array[3:7, 3:7, 0:1]
        np.testing.assert_array_equal(result, expected)

    def test_full_size_crop(self):
        result = zoom_me(self.small_array, 10)
        self.assertEqual(result.shape, (10, 10, 1))

    def test_default_size_used(self):
        big_array = np.zeros((500, 500, 3), dtype=np.uint8)
        result = zoom_me(big_array)
        self.assertEqual(result.shape, (400, 400, 1))

    def test_size_too_big_raises(self):
        with self.assertRaises(ValueError):
            zoom_me(self.small_array, 20)

    def test_invalid_array_type(self):
        with self.assertRaises(TypeError):
            zoom_me([[1, 2], [3, 4]], 1)

    def test_1d_array_raises(self):
        with self.assertRaises(TypeError):
            zoom_me(np.array([1, 2, 3]), 1)

    def test_dtype_preserved(self):
        array = np.zeros((20, 20, 3), dtype=np.uint8)
        result = zoom_me(array, 5)
        self.assertEqual(result.dtype, array.dtype)


if __name__ == "__main__":
    unittest.main()