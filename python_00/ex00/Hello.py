# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   Hello.py                                           :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/05 02:21:02 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/05 02:50:51 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

ft_tuple = (ft_tuple[0], "Brazil!")

ft_set.remove("tutu!")
ft_set.add("Rio de Janeiro!")

ft_dict["Hello"] = "42Rio!"

print(ft_list)
print(ft_tuple)
print(ft_set) 
print(ft_dict)