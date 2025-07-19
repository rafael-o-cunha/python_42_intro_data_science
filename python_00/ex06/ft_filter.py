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

"""
    -> filtrar pelo len maior que o recebido
    -> validar caracteres da palavra (palavra não visível ou pontuação)
    -> trocar implementação por lambda e list comprehension
"""

def ft_filter(data: str, size: int) -> list:
    splited_data = data.split(' ')
    return splited_data