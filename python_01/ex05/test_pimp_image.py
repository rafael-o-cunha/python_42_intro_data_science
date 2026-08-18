import unittest
import numpy as np
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


class TestFtInvert(unittest.TestCase):
    """Independent tests for ft_invert, using a synthetic array."""

    def setUp(self):
        self.array = np.array(
            [[[0, 100, 255], [50, 200, 10]]], dtype=np.uint8
        )

    def test_returns_ndarray(self):
        result = ft_invert(self.array)
        self.assertIsInstance(result, np.ndarray)

    def test_shape_preserved(self):
        result = ft_invert(self.array)
        self.assertEqual(result.shape, self.array.shape)

    def test_values_are_inverted(self):
        result = ft_invert(self.array)
        expected = 255 - self.array
        np.testing.assert_array_equal(result, expected)

    def test_dtype_preserved(self):
        result = ft_invert(self.array)
        self.assertEqual(result.dtype, self.array.dtype)

    def test_double_invert_returns_original(self):
        result = ft_invert(ft_invert(self.array))
        np.testing.assert_array_equal(result, self.array)

    def test_not_ndarray_raises(self):
        with self.assertRaises(TypeError):
            ft_invert([[1, 2, 3]])


class TestFtRed(unittest.TestCase):
    """Independent tests for ft_red."""

    def setUp(self):
        self.array = np.array(
            [[[10, 20, 30], [40, 50, 60]]], dtype=np.uint8
        )

    def test_shape_preserved(self):
        result = ft_red(self.array)
        self.assertEqual(result.shape, self.array.shape)

    def test_keeps_only_red_channel(self):
        result = ft_red(self.array)
        np.testing.assert_array_equal(result[:, :, 0], self.array[:, :, 0])
        self.assertTrue((result[:, :, 1] == 0).all())
        self.assertTrue((result[:, :, 2] == 0).all())

    def test_not_ndarray_raises(self):
        with self.assertRaises(TypeError):
            ft_red("not an array")


class TestFtGreen(unittest.TestCase):
    """Independent tests for ft_green."""

    def setUp(self):
        self.array = np.array(
            [[[10, 20, 30], [40, 50, 60]]], dtype=np.uint8
        )

    def test_shape_preserved(self):
        result = ft_green(self.array)
        self.assertEqual(result.shape, self.array.shape)

    def test_keeps_only_green_channel(self):
        result = ft_green(self.array)
        np.testing.assert_array_equal(result[:, :, 1], self.array[:, :, 1])
        self.assertTrue((result[:, :, 0] == 0).all())
        self.assertTrue((result[:, :, 2] == 0).all())

    def test_original_array_not_mutated(self):
        original = self.array.copy()
        ft_green(self.array)
        np.testing.assert_array_equal(self.array, original)

    def test_not_ndarray_raises(self):
        with self.assertRaises(TypeError):
            ft_green(None)


class TestFtBlue(unittest.TestCase):
    """Independent tests for ft_blue."""

    def setUp(self):
        self.array = np.array(
            [[[10, 20, 30], [40, 50, 60]]], dtype=np.uint8
        )

    def test_shape_preserved(self):
        result = ft_blue(self.array)
        self.assertEqual(result.shape, self.array.shape)

    def test_keeps_only_blue_channel(self):
        result = ft_blue(self.array)
        np.testing.assert_array_equal(result[:, :, 2], self.array[:, :, 2])
        self.assertTrue((result[:, :, 0] == 0).all())
        self.assertTrue((result[:, :, 1] == 0).all())

    def test_not_ndarray_raises(self):
        with self.assertRaises(TypeError):
            ft_blue(123)


class TestFtGrey(unittest.TestCase):
    """Independent tests for ft_grey."""

    def setUp(self):
        self.array = np.array(
            [[[9, 30, 60], [0, 0, 0], [255, 255, 255]]], dtype=np.uint8
        )

    def test_shape_preserved(self):
        result = ft_grey(self.array)
        self.assertEqual(result.shape, self.array.shape)

    def test_channels_are_equal(self):
        result = ft_grey(self.array)
        np.testing.assert_array_equal(result[:, :, 0], result[:, :, 1])
        np.testing.assert_array_equal(result[:, :, 1], result[:, :, 2])

    def test_correct_average_value(self):
        result = ft_grey(self.array)
        # (9 + 30 + 60) // 3 == 33
        self.assertEqual(result[0, 0, 0], 33)
        self.assertEqual(result[0, 1, 0], 0)
        self.assertEqual(result[0, 2, 0], 255)

    def test_not_ndarray_raises(self):
        with self.assertRaises(TypeError):
            ft_grey([1, 2, 3])


if __name__ == "__main__":
    unittest.main()