# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   docs.py                                            :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/05 22:42:11 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/18 22:56:03 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #


def py_doc(docstring):
    """
        Description:
            Function to manage docstrings

        Args:
            docstring (str): A docstring of a function
            in the project.

        Returns: Result of interpreted docstring when
        builtin (__doc__) is invoked.

    """
    def decorator(func):
        func.__doc__ = docstring
        return func
    return decorator


FT_FILTER = """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item)
    is true. If function is None, return the items that are true.
"""


MAIN = """
    Args:
        S (str): A string containing words separated by spaces.
        N (int): The length limit (len > N).

    Returns:
        list: A list of words that meet the criteria.
"""


FT_MY_FILTER = """
    Validate string length and character content.

    Returns True if string is longer than size and contains no control
    characters, invisible characters, or punctuation marks.
"""
