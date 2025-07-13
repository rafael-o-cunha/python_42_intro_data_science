# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   find_ft_type.py                                    :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/11 22:00:48 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/11 22:40:13 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    collected_type = type(object)
    dict_of_types = {list : "List :",
                    tuple : "Tuple :",
                    set : "Set :", 
                    dict : "Dict :",
                    str : "is in the kitchen :"}

    if collected_type != str and collected_type != int:
        print(f"{dict_of_types.get(collected_type, 'Type not found')} {collected_type}")
    elif collected_type == str:
        print(f"{object} {dict_of_types.get(collected_type, 'Type not found')} {collected_type}")
    else:
        print("Type not found")
    return 42