# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   NULL_not_found.py.py                               :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/05 22:42:11 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/12 20:47:03 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

def NULL_not_found(object: any) -> int:
    collected_type = type(object)

    if collected_type == type(None):
        print(f"Nothing: None {collected_type}")
        return 0
    elif collected_type == type(float("NaN")):
        print(f"Cheese: nan {collected_type}")
        return 0
    elif collected_type == type(0):
        print(f"Zero: 0 {collected_type}")
        return 0
    elif collected_type == type("") and collected_type == "":
        print(f"Empty: {collected_type}")
        return 0
    elif collected_type == type(False):
        print(f"Fake: False {collected_type}")
        return 0
    else:
        print("Type not found")
    return 1