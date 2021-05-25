import numpy as np

two_dim_array = np.array([[11, 15, 10, 6],
                          [10, 14, 11, 5],
                          [12, 17, 12, 8],
                          [15, 18, 14, 9]])
                          
print(two_dim_array)

def access_elements(array, row_index, col_index):
    if row_index >= len(array) and col_index >= len(array[0]):
        print("Incorrect index.")
    else:
        print(array[row_index][col_index])

print("\nAccessing an element:")
access_elements(two_dim_array, 1, 2)