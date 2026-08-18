import unittest
import numpy as np
from rotate import crop_square, ft_transpose


class TestCropSquare(unittest.TestCase):
    """Independent tests for crop_square. Uses a synthetic array instead
    of a real loaded image."""

    def setUp(self):
        # Deterministic 10x10x3 array to check the crop values precisely.
        self.small_array = np.arange(10 * 10 * 3).reshape(10, 10, 3)

    def test_returns_ndarray(self):
        result = crop_square(self.small_array, 4)
        self.assertIsInstance(result, np.ndarray)

    def test_correct_shape(self):
        result = crop_square(self.small_array, 4)
        self.assertEqual(result.shape, (4, 4, 1))

    def test_keeps_single_channel(self):
        result = crop_square(self.small_array, 4)
        expected = self.small_array[3:7, 3:7, 0:1]
        np.testing.assert_array_equal(result, expected)

    def test_full_size_crop(self):
        result = crop_square(self.small_array, 10)
        self.assertEqual(result.shape, (10, 10, 1))

    def test_default_size_used(self):
        big_array = np.zeros((500, 500, 3), dtype=np.uint8)
        result = crop_square(big_array)
        self.assertEqual(result.shape, (400, 400, 1))

    def test_size_too_big_raises(self):
        with self.assertRaises(ValueError):
            crop_square(self.small_array, 20)


class TestFtTranspose(unittest.TestCase):
    """Independent tests for ft_transpose (manual transpose, no library
    transpose method used inside it)."""

    def test_square_array(self):
        array = np.array([[1, 2], [3, 4]])
        result = ft_transpose(array)
        expected = np.array([[1, 3], [2, 4]])
        np.testing.assert_array_equal(result, expected)

    def test_rectangular_array(self):
        array = np.array([[1, 2, 3], [4, 5, 6]])
        result = ft_transpose(array)
        self.assertEqual(result.shape, (3, 2))
        np.testing.assert_array_equal(result, array.T)

    def test_matches_numpy_transpose(self):
        array = np.arange(20).reshape(4, 5)
        result = ft_transpose(array)
        np.testing.assert_array_equal(result, array.transpose())

    def test_dtype_preserved(self):
        array = np.zeros((3, 3), dtype=np.uint8)
        result = ft_transpose(array)
        self.assertEqual(result.dtype, array.dtype)

    def test_not_ndarray_raises(self):
        with self.assertRaises(TypeError):
            ft_transpose([[1, 2], [3, 4]])

    def test_1d_array_raises(self):
        with self.assertRaises(TypeError):
            ft_transpose(np.array([1, 2, 3]))

    def test_3d_array_raises(self):
        with self.assertRaises(TypeError):
            ft_transpose(np.zeros((2, 2, 3)))

    def test_double_transpose_returns_original(self):
        array = np.arange(12).reshape(3, 4)
        result = ft_transpose(ft_transpose(array))
        np.testing.assert_array_equal(result, array)


if __name__ == "__main__":
    unittest.main()