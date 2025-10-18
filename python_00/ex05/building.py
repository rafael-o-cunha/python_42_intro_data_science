# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   building.py                                        :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/13 15:44:23 by rafade-o          #+#    #+#             #
#   Updated: 2025/10/17 22:47:18 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys


def count_itens_inside_data_and_print(data: str):
    """
        Counts the number of upper, lower, punctuation, spaces, and digit
        characters.

        Args:
            text: The text to analyze.
    """
    total_chars = len(data)
    spaces = data.count(" ")
    upper_letters = 0
    lower_letters = 0
    punctuation_marks = 0
    digits = 0

    i = 0
    while i < total_chars:
        character = data[i]
        if character.isdigit() or character.isnumeric():
            digits += 1
        elif character.isalpha():
            if character.islower() and character != ' ':
                lower_letters += 1
            elif character.isupper() and character != ' ':
                upper_letters += 1
        elif character != ' ':
            punctuation_marks += 1
        i += 1

    message = f"""The text contains {total_chars} characters:
{upper_letters} upper letters
{lower_letters} lower letters
{punctuation_marks} punctuation marks
{spaces} spaces
{digits} digits"""

    print(message)


def main():
    """
        Args:
            S (str): A string containing words separated by spaces.

        Print:
            The information about (S) with: number of chars,
            spaces, upper and lower chars, punctuations and digits.
    """
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
