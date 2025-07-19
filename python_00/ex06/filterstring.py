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

    filtered_data = ft_filter(data, size)
    print(filtered_data)
    return


if __name__ == "__main__":
    main()
