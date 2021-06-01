# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100.
# Example: missing_number([1,2,3,4,6], 6) # Returns: 5

import numpy as np

my_list = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
           71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
           91, 92, 93, 94, 95, 96, 97, 98,  100]

def missing_number(list, n):

    sum_list = sum(list)

    sum_n = n*(n+1)/2

    return sum_n - sum_list

print("\n", missing_number(my_list, 100))