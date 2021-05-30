# Project 6 - Rotate Matrix
# Given an image represented by an NxM matrix write a method to rotate
# the image by 90 degrees.

# 1 2 3         7 4 1
# 4 5 6  ---->  8 5 2
# 7 8 9         9 6 3

# for i = 0 to n
#   temp = top[i]
#   top[i] = left[i]
#   left[i] = botton[i]
#   botton[i] = right[i]
#   right[i] = temp

import numpy as np

my_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(my_array)

def rotate_matrix(matrix):
    n = len(matrix)

    # Define matrix layers
    for layer in range(n//2):
        first = layer
        last = n - first - 1

        for i in range(first,last):
            # Save top element
            top = matrix[layer][i]
            # Move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # Move botton element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # Move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # Move to right
            matrix[i][-layer-1] = top
        
        return matrix

print(rotate_matrix(my_array))