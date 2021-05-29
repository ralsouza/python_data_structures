# Question 5 - Is Unique: 
# Implement an algorithm to determine if a list has all unique characters, using Python list.

# Tips:
# Step 1: Create empty list
# Step 2: Loop through given list
# Step 3: In each visit check if the visited element is in our newly created list and save the visited
# element in the newly create list.

my_list = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]

def is_unique(array):
    
    unique_list = []
    
    for i in array:
        if i in unique_list:
            print(f"Duplicated value: {i}")
            return False
        else:
            unique_list.append(i)
    return True

is_unique(my_list)