# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_filter.py                                       :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+     d      #
#   Created: 2025/07/05 22:42:11 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/18 22:56:03 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #


def ft_filter(function, iterable):
    """
        filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of iterable for which
        function(item)
        is true. If function is None, return the items that are true.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
