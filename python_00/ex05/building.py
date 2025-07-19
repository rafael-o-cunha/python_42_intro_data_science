# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   building.py                                        :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/13 15:44:23 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/18 22:57:18 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys
from count_itens_inside_data_and_print import count_itens_inside_data_and_print


def main():
    argc = sys.argv.__len__()

    if argc == 2:
        data = sys.argv[1]
    elif argc < 2:
        while 1:
            data = input("What is the text to count?\n")

            if len(data) != 0:
                data = f"{data} "
                break
    else:
        print("AssertionError.")

    try:
        count_itens_inside_data_and_print(data)
        return
    except Exception:
        print(f"AssertionError: {Exception.with_traceback()}")


if __name__ == "__main__":
    main()
