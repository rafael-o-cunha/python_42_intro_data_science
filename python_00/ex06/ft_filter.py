# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_filter.py                                       :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/05 22:42:11 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/18 22:56:03 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #
from docs import py_doc, FT_FILTER


@py_doc(FT_FILTER)
def ft_filter(function, iterable):
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
