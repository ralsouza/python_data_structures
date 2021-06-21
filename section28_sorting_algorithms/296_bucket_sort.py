# Bucket Sort
# - Create buckets and distribute element of array into buckets
# - Sort buckets individually
# - Merge buckets after sorting
# - Number of buckets = round(Sqrt(number of elements))
#   Ex: roung(Sqrt(9)) = 3
# - Appropriate bucket = ceil(value * number of buckets / max_value)
#   ceil(5*3/9) = ceil(1.6) = 2

from math import sqrt, ceil

def insertion_sort(custom_list):
    for i in range(1,len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -= 1
        custom_list[j+1] = key
    print(custom_list)

def bucket_sort(customList):
    numberofBuckets = round(sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    
    for i in range(numberofBuckets):
        arr[i] = insertion_sort(arr[i])
    
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

    return custom_list

c_list = [2,1,7,6,5,3,4,9,8]

bucket_sort(c_list)