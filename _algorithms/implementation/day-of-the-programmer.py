#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

jan_days = 31
march_days = 31
april_days = 30
may_days = 31
june_days = 30
july_days = 31
august_days = 31
september_days = 30
october_days = 31
november_days = 30
decemeber_days = 31

month_days = [jan_days, 0, march_days, april_days, 
              may_days, june_days, july_days, august_days,
              september_days, october_days, november_days, decemeber_days]

def get_feb_days_julian(year):
    if year % 4 == 0:
        return 29 #leap year
    else:
        return 28 #not leap year

def get_feb_days_gregorian(year):
   
    if year % 400 == 0:
        return 29 #leap year
    elif year % 100 == 0:
        return 28 #not leap year
    elif year % 4 == 0:
        return 29 #leap year
    else:
        return 28 #not leap year

# Complete the solve function below.
def solve(year):
    
    if year <= 1917: #implicitly also year >= 1700
        feb_days = get_feb_days_julian(year)
    elif year == 1918:
        feb_days = get_feb_days_gregorian(1918) - 13 #transition
    else: #1919 <= year <= 2700
        feb_days = get_feb_days_gregorian(year)
        
    month_days[1] = feb_days
    
    found_month = False
    cur_days = 0
    next_month = 1
    programmer_month = -1 #not set
    programmer_day = -1 #not set
    while not found_month: #find day 256
        next_month_days = month_days[next_month-1] #0-based indexing
        if cur_days + next_month_days >= 256:
            found_month = True
            programmer_month = next_month
            #cur_days + programmer_day = 256; know programmer day in next_month
            programmer_day = 256 - cur_days 
        else:
            cur_days += next_month_days
            next_month += 1
         
    day_of_the_programmer = "{:02}.{:02}.{}".format(programmer_day, programmer_month, year)  
    print(day_of_the_programmer)
    return(day_of_the_programmer)

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input())
    result = solve(year)

    fptr.write(result + '\n')
    fptr.close()

