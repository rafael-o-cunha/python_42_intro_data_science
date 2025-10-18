# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   filterstring.py                                    :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/13 15:44:23 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/18 22:57:18 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys
from ft_filter import ft_filter


def ft_my_filter(data: str, size: int) -> bool:
    """
        Validate string length and character content.

        Returns True if string is longer than size and contains no control
        characters, invisible characters, or punctuation marks.
    """
    punctuations = r"%&'()*+,-./:;<=>?@[\]^_`{|}~"

    if len(data) <= size:
        return False

    for c in data:
        if ord(c) in range(0, 32) or ord(c) in range(127, 160):
            return False
        if ord(c) in range(173, 256):
            return False
        elif punctuations.find(c) != -1:
            return False
    return True


def main():
    """
        Args:
            S (str): A string containing words separated by spaces.
            N (int): The length limit (len > N).

        Returns:
            list: A list of words that meet the criteria.
    """
    argc = sys.argv.__len__()

    if argc == 3:
        data = sys.argv[1]
        size = sys.argv[2]
    else:
        print('AssertionError: the arguments are bad')
        return

    if not size.isdigit() or not size.isnumeric():
        print('AssertionError: the arguments are bad')
        return

    size = int(size)
    lambda word: (len(word) >= size)

    data_list = data.split(' ')
    filtered_data = ft_filter(lambda word: ft_my_filter(word, size), data_list)

    print(filtered_data)
    return


if __name__ == "__main__":
    main()
