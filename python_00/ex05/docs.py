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


COUNT_ITENS_INSIDE_DATA_AND_PRINT = """
    Counts the number of upper, lower, punctuation, spaces, and digit
    characters.

    Args:
        text: The text to analyze.
"""

MAIN = """
    Args:
        S (str): A string containing words separated by spaces.

    Print:
        The information about (S) with: number of chars,
        spaces, upper and lower chars, punctuations and digits.
"""
