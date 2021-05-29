# Project 4 - How to find maxium product of two integers in the array
#             where all elements are positive.

import numpy as np

my_array = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

def max_prod(array):
    
    max_prod = 0

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]*array[j] > max_prod:
                max_prod = array[i]*array[j]
                pair = f"{array[i]}, {array[j]}"

    print(f"Pair: {pair}\nMax Prod: {max_prod}")

max_prod(my_array) 