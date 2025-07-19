# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   count_itens_inside_data_and_print.py.py            :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/05 22:42:11 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/18 22:56:03 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

def count_itens_inside_data_and_print(data: str):
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
