# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   whatis.py                                          :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/12 20:51:19 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/12 21:13:02 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys


def main():
    argc = sys.argv.__len__()

    if argc == 2:
        try:
            data = sys.argv[1]
            int_data = int(data)
            print("I'm Even." if int_data % 2 == 0 else "I'm Odd.")
        except Exception:
            print("AssertionError: argument is not an integer")
        return

    if argc > 2:
        print("AssertionError: more than one argument is provided")
    else:
        print()


if __name__ == "__main__":
    main()
