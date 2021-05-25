import numpy as np
from numpy.lib.shape_base import column_stack

two_dim_array = np.array([[11, 15, 10, 6],
                          [10, 14, 11, 5],
                          [12, 17, 12, 8],
                          [15, 18, 14, 9]])
                          
print(two_dim_array)

# .insert(array, position, list_elements, axis=(0-row | 1-col))
new_two_dim_array = np.insert(two_dim_array, 1, [[1,2,3,4]], axis=0)
print(new_two_dim_array)

# .append() method - Insert at the end
new_two_dim_array2 = np.append(two_dim_array, [[1,2,3,4]], axis=0)
print(new_two_dim_array2)