# Project 3 - Finding a number in a array
# Question 3 - How to check if an array contains a number in Python

import numpy as np

my_list = list(range(1,21))
my_array = np.array(my_list)

def find_number(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(f"The number {number} exists at index {i}.")

find_number(my_array, 13)
find_number(my_array, 21)