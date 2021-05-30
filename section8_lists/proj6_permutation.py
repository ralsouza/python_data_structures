# Question 6 - Permutation

def permutation(list1, list2):

    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


list1 = [1,2,3]
list2 = [1,3,2]

list4 = ["a","c","b"]
list5 = ["c","a","b"]
list6 = ["c","a","d"]

print(permutation(list1,list2))
print(permutation(list4,list5))
print(permutation(list4,list6))