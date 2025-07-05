"""
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   format_ft_time.py                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rafade-o <rafade-o@student.42.rio>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/05 03:17:29 by rafade-o          #+#    #+#             */
/*   Updated: 2025/07/05 03:32:51 by rafade-o         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
"""

from datetime import date, datetime
from time import ctime

initial_date = datetime.strptime('01/01/1970', '%m/%d/%Y').date()
today = datetime.now()

print(initial_date)
print(today)
print()

seconds = 0
e_seconds = 0

print(f'Seconds since January 1, 1970: {seconds} or {e_seconds} in scientific notation')

current_day = date.today().day
current_month_formated = date.today().strftime("%B")
current_year = date.today().year

print(f'{current_month_formated} {current_day} {current_year}')