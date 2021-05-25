import numpy as np

two_dim_array = np.array([[11, 15, 10, 6],
                          [10, 14, 11, 5],
                          [12, 17, 12, 8],
                          [15, 18, 14, 9]])
                          
print(two_dim_array)

# Delete fisrt row
new_td_array = np.delete(two_dim_array, 0, axis=0)

print("\nNew array without first row:")
print(new_td_array)

# Delete first column
new_td_array = np.delete(two_dim_array, 0, axis=1)

print("\nNew array without first column:")
print(new_td_array)

# Delete second column
new_td_array = np.delete(two_dim_array, 0, axis=1)

print("\nNew array without second column:")
print(new_td_array)

