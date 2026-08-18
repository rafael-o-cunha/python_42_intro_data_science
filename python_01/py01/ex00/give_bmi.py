def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    - function: give_bmi
        receives:
            height: list of int or float, heights in meters
            weight: list of int or float, weights in kilograms
        returns:
            list of int or float: the calculated BMI values (weight / height²)
        handles:
            ValueError: if the lists do not have the same length
            TypeError: if the inputs are not lists or contain values
            that are not int or float
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")

    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")

    for value in height + weight:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("height and weight must only contain int or float")

    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    - function: apply_limit
        receives:
            list of integers or floats and an integer representing param limit
        returns:
            list of booleans (true if below the limit)
        handles:
            error if lists have different sizes
            error if the list data types are not int or float
    """

    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")

    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an int")

    for value in bmi:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("bmi must only contain int or float")
    return [value > limit for value in bmi]


def main():
    """Test give_bmi and apply_limit with the example from the subject."""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
