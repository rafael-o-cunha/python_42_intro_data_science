import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of an image by subtracting each pixel value from
    the maximum possible value (255).

    Parameters:
        array: numpy.ndarray, the image pixel content (H, W, 3)

    Returns:
        numpy.ndarray: the image with inverted colors, same shape/dtype

    Raises:
        TypeError: if array is not a numpy.ndarray
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy ndarray")

    result = array.astype(np.int16)
    result = 255 - result
    return result.astype(array.dtype)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keep only the red channel of an image, setting the other channels
    to 0.

    Parameters:
        array: numpy.ndarray, the image pixel content (H, W, 3)

    Returns:
        numpy.ndarray: the image with only the red channel kept,
            same shape/dtype

    Raises:
        TypeError: if array is not a numpy.ndarray
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy ndarray")

    mask = np.array([1, 0, 0], dtype=array.dtype)
    result = array * mask
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keep only the green channel of an image, setting the other channels
    to 0.

    Parameters:
        array: numpy.ndarray, the image pixel content (H, W, 3)

    Returns:
        numpy.ndarray: the image with only the green channel kept,
            same shape/dtype

    Raises:
        TypeError: if array is not a numpy.ndarray
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy ndarray")

    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keep only the blue channel of an image, setting the other channels
    to 0.

    Parameters:
        array: numpy.ndarray, the image pixel content (H, W, 3)

    Returns:
        numpy.ndarray: the image with only the blue channel kept,
            same shape/dtype

    Raises:
        TypeError: if array is not a numpy.ndarray
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy ndarray")

    result = np.zeros(array.shape, dtype=array.dtype)
    result[:, :, 2] = array[:, :, 2]
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert an image to greyscale by averaging its three color
    channels and applying the result to all channels.

    Parameters:
        array: numpy.ndarray, the image pixel content (H, W, 3)

    Returns:
        numpy.ndarray: the greyscale image, same shape/dtype

    Raises:
        TypeError: if array is not a numpy.ndarray
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy ndarray")

    total = array.sum(axis=2, dtype=np.int32)
    grey = total / 3
    grey = grey.astype(array.dtype)
    result = np.empty(array.shape, dtype=array.dtype)
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return result


def main():
    """
    Test the 5 filters on landscape.jpg and display them.
    """
    try:
        import matplotlib.pyplot as plt
        from load_image import ft_load

        array = ft_load("../assets/landscape.jpg")

        inverted = ft_invert(array)
        red = ft_red(array)
        green = ft_green(array)
        blue = ft_blue(array)
        grey = ft_grey(array)

        print(ft_invert.__doc__)

        fig, axes = plt.subplots(3, 2, figsize=(8, 10))
        titles = ["Original", "Invert", "Red", "Green", "Blue", "Grey"]
        images = [array, inverted, red, green, blue, grey]
        for ax, title, img in zip(axes.flat, titles, images):
            ax.imshow(img)
            ax.set_title(title)

        plt.tight_layout()
        plt.savefig("pimp_output.png")
        print("Image saved as pimp_output.png")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
