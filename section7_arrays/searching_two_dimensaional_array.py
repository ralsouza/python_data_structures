import numpy as np

two_dim_array = np.array([[11, 15, 10, 6],
                          [10, 14, 11, 5],
                          [12, 17, 12, 8],
                          [15, 18, 14, 9]])
                          
print(two_dim_array)

def search_td_array(array, value):
    """ 
        Linear search.
    """
    # Space Complexity: O(1)
    for i in range(len(array)): # --------------------------------> O(mn)
        for j in range(len(array[0])): # -------------------------> O(n)
            if array[i][j] == value: # ---------------------------> O(1)
                return f"The value is located at index {i}x{j}"
    return "The element was not found."

print("\n")

print(search_td_array(two_dim_array, 80))