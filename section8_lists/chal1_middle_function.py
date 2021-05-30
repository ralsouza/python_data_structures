# Middle Function
# Write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements.

my_list = [1,2,3,4]
# Ex: middle(my_list) >> returns [2,3]

def middle(list):
    return list[1:-1]