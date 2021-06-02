# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number.
# Example: pair_sum([2,4,3,5,6,-2,4,7,8,9], 7)
# Output: ['2+5', '4+3', '3+4', '-2+9']

my_list = [2,4,3,5,6,-2,4,7,8,9]

def pair_sum(list, num_sum):
    output = []

    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == num_sum:
                # print(f"{list[i]} + {list[j]} = {num_sum}")
                output.append(f"{list[i]}+{list[j]}")

    return output

print(pair_sum(my_list, 7))