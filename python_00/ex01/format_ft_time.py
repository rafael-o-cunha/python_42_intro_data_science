# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   format_ft_time.py                                  :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2025/07/05 03:17:29 by rafade-o          #+#    #+#             #
#   Updated: 2025/07/11 21:57:57 by rafade-o         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import time
import datetime

timestamp = time.time()
seconds = f"{timestamp:,.4f}"
e_seconds = f"{timestamp:.2e}"

print(f'Seconds since January 1, 1970: {seconds} or {e_seconds} in scientific notation')

date = datetime.datetime.fromtimestamp(timestamp)
print(date.strftime("%b %d %Y"))