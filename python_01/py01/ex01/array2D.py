def slice_me(family: list, start: int, end: int) -> list:
    """
    - Print the shape of a 2D list (as rows, cols) and return a slice
    of its rows between start and end (using list slicing).

    Parameters:
        family: list, a 2D list (list of lists of the same length)
        start: int, start index for the slice
        end: int, end index for the slice

    Returns:
        list: the truncated 2D list, family[start:end]

    Raises:
        TypeError: if family is not a list, or is not a proper 2D list,
                or if start/end are not int
        ValueError: if the rows don't all have the same length
    """

    if not isinstance(family, list) or len(family) == 0:
        raise TypeError("family must be a non-empty list")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists (2D array)")
    row_len = len(family[0])

    if not all(len(row) == row_len for row in family):
        raise ValueError("all rows in family must have the same size")

    if isinstance(start, bool) or not isinstance(start, int):
        raise TypeError("start must be an int")

    if isinstance(end, bool) or not isinstance(end, int):
        raise TypeError("end must be an int")

    print(f"My shape is : ({len(family)}, {row_len})")
    new_family = family[start:end]
    new_row_len = len(new_family[0]) if new_family else 0
    print(f"My new shape is : ({len(new_family)}, {new_row_len})")
    return new_family


def main():
    """Test slice_me with the example from the subject."""
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]

        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
