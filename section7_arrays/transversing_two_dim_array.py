import numpy as np

two_dim_array = np.array([[11, 15, 10, 6],
                          [10, 14, 11, 5],
                          [12, 17, 12, 8],
                          [15, 18, 14, 9]])
                          
print(two_dim_array)

# Space complexity: O(1)
def transverse_td_array(array):
    for i in range(len(array)): # ------------> O(mn)
        for j in range(len(array[0])): # -----> O(n)
            print(array[i][j]) # -------------> O(1)

transverse_td_array(two_dim_array)