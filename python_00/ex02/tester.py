# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   tester.py                                          :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/11 22:00:48 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/11 22:40:36 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

