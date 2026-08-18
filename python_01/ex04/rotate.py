import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def crop_square(array: np.ndarray, size: int = 400) -> np.ndarray:
    """
    Crop a square area of `size` x `size` pixels centered on the image,
    keeping only one channel, shape (size, size, 1).

    Parameters:
        array: numpy.ndarray, the source image (H, W, C)
        size: int, side length in pixels of the square to extract

    Returns:
        numpy.ndarray: the cropped array of shape (size, size, 1)

    Raises:
        ValueError: if the image is smaller than the requested size
    """
    height, width = array.shape[0], array.shape[1]
    if height < size or width < size:
        raise ValueError("image is too small for the requested crop size")

    start_y = (height - size) // 2
    start_x = (width - size) // 2
    return array[start_y:start_y + size, start_x:start_x + size, 0:1]


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """
    Transpose a 2D array manually (no library transpose method allowed):
    swap rows and columns by hand.

    Parameters:
        array: numpy.ndarray, a 2D array of shape (rows, cols)

    Returns:
        numpy.ndarray: a new array of shape (cols, rows)

    Raises:
        TypeError: if array is not a 2D numpy.ndarray
    """
    if not isinstance(array, np.ndarray) or array.ndim != 2:
        raise TypeError("array must be a 2D numpy ndarray")

    rows, cols = array.shape
    result = np.empty((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = array[i][j]

    return result


def main():
    """Load animal.jpeg, crop it, transpose it manually and display it."""
    try:
        array = ft_load("../assets/animal.jpeg")

        cropped = crop_square(array, 400)
        squeezed = cropped.squeeze(axis=2)
        print(f"The shape of image is: {cropped.shape} or {squeezed.shape}")
        print(cropped)

        transposed = ft_transpose(squeezed)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        plt.imshow(transposed, cmap="gray")
        plt.title("Transposed animal")
        plt.savefig("rotate_output.png")
        print("Image saved as rotate_output.png")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
