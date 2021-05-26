# Accessing/Transversing the list

shop_list = ["Milk","Cheese","Butter"]

# in operator
print("Milk" in shop_list)

print("Bread" in shop_list)

# Negative indexes
print(shop_list[-2])

# Transversing list by list elements
print("\nTransversing List:")
for i in shop_list:
    print(i)

# Transversion list by range method and changing strings
print("\nTransversin List:")
for i in range(len(shop_list)):
    shop_list[i] = shop_list[i] + "+"
    print(shop_list[i])