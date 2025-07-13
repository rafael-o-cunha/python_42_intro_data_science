# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   tester.py                                          :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/11 22:44:27 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/12 20:48:17 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))