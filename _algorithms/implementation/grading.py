#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def round_grade(grade):
    
    if grade <= 37:
        return grade
    
    else:
        ones = grade % 10
        if ones <= 2 or (ones >= 5 and ones <= 7):
            return grade
        else:
            tens = grade - ones
            if (ones == 3 or ones == 4):
                return tens + 5
            else: #ones = 8 or 9
                return tens + 10
        

def gradingStudents(grades):
    #
    # Write your code here.
    #
    modified_grades = [round_grade(grade) for grade in grades]
    
    for mod_grade in modified_grades:
        print(mod_grade)
        
    return modified_grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

