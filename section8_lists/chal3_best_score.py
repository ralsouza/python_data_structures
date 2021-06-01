# Best Score
# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.

my_list = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(my_list) --> returns 90 87

def first_second(list):

    sorted_list = sorted(list, reverse=True)
    
    best_scores = sorted_list[:2]

    return tuple(best_scores)
        
print(first_second(my_list))


