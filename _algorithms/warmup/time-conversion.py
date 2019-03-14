#!/bin/python3

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    res = re.match("\d{2}:\d{2}:\d{2}(AM|PM)", s)
    assert(res)
   
    is_PM = False
    hour, minute, second = s.split(sep = ":")

    if "PM" in second:
        is_PM = True
    
    hour_int = int(hour)
    if hour_int == 12:
        hour_int = 0 #since e.g. 12PM -> 12:00:00 and 12AM -> 0:00:00
        
    second = second[:-2]
    
    military_time = ""
    if is_PM:
        military_time +="{0:02d}:".format(hour_int+12)
    else:
        military_time += "{0:02d}:".format(hour_int) 
    
    military_time += minute + ":"
    military_time += second
     
    print(military_time)   
    
    return(military_time)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

