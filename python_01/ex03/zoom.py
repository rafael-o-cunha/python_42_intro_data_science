import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_me(array: np.ndarray, size: int = 400) -> np.ndarray:
    """
    Crop a square area of `size` x `size` pixels centered on the image,
    keep only one channel (as a (size, size, 1) array), using slicing.

    Parameters:
        array: numpy.ndarray, the source image (H, W, C)
        size: int, the side length in pixels of the square to extract

    Returns:
        numpy.ndarray: the cropped array of shape (size, size, 1)

    Raises:
        ValueError: if the image is smaller than the requested size
    """
    if not isinstance(array, np.ndarray) or array.ndim < 2:
        raise TypeError("array must be a numpy ndarray with at least 2 dims")
    height, width = array.shape[0], array.shape[1]

    if height < size or width < size:
        raise ValueError("image is too small for the requested zoom size")

    start_y = (height - size) // 2
    start_x = (width - size) // 2

    cropped = array[start_y:start_y + size, start_x:start_x + size, 0:1]
    return cropped


def main():
    """
    Load animal.jpeg, print info and display it zoomed.
    """
    try:
        array = ft_load("../assets/animal.jpeg")
        print(array)

        zoomed = zoom_me(array, 400)
        print(f"New shape after slicing: {zoomed.shape} or "
              f"{zoomed.squeeze(axis=2).shape}")
        print(zoomed)

        plt.imshow(zoomed.squeeze(axis=2), cmap="gray")
        plt.title("Zoomed animal")
        plt.savefig("zoom_output.png")
        print("Image saved as zoom_output.png")
        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
