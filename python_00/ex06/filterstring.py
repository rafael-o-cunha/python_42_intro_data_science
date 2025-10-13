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
from docs import py_doc, MAIN, FT_MY_FILTER


@py_doc(FT_MY_FILTER)
def ft_my_filter(data: str, size: int) -> bool:
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


@py_doc(MAIN)
def main():
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
