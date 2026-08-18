import unittest
import numpy as np
from load_image import ft_load


class TestFtLoad(unittest.TestCase):
    path = "../assets/landscape.jpg"
    def test_returns_ndarray(self):
        result = ft_load(self.path)
        self.assertIsInstance(result, np.ndarray)

    def test_correct_shape(self):
        result = ft_load(self.path)
        self.assertEqual(len(result.shape), 3)
        self.assertEqual(result.shape[2], 3)

    def test_rgb_channels(self):
        result = ft_load(self.path)
        self.assertEqual(result.shape[2], 3)

    def test_dtype_uint8(self):
        result = ft_load(self.path)
        self.assertEqual(result.dtype, np.uint8)

    def test_pixel_value_range(self):
        result = ft_load(self.path)
        self.assertTrue((result >= 0).all())
        self.assertTrue((result <= 255).all())

    def test_file_not_found(self):
        with self.assertRaises(Exception):
            ft_load("does_not_exist.jpg")

    def test_invalid_path_type(self):
        with self.assertRaises(Exception):
            ft_load(12345)

    def test_none_path(self):
        with self.assertRaises(Exception):
            ft_load(None)

    def test_invalid_image_content(self):
        with self.assertRaises(Exception):
            ft_load("fake.jpg")

    def test_empty_path(self):
        with self.assertRaises(Exception):
            ft_load("")


if __name__ == "__main__":
    unittest.main()