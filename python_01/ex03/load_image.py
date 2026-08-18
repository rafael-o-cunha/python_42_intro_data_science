import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image file and return its pixel content as a numpy array
    in RGB format. Also prints the shape of the loaded image.

    Parameters:
        path: str, the path to the image file (jpg/jpeg at least)

    Returns:
        numpy.ndarray: the pixel content of the image (H, W, 3)

    Raises:
        FileNotFoundError: if the file does not exist
        ValueError: if the file cannot be opened as an image
    """
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            array = np.array(img)
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file: '{path}'")
    except Exception as e:
        raise ValueError(f"Could not load image '{path}': {e}")

    print(f"The shape of image is: {array.shape}")
    return array


def main():
    """Test ft_load with the landscape.jpg example."""
    try:
        array = ft_load("landscape.jpg")
        print(array)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
