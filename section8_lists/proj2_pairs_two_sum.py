# Project 2 - Find Pairs
# (2,2) or (3,3) not valid pairs

def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i,j) 

my_list = [1,2,3,2,3,4,5,6]

find_pairs(my_list, 6)