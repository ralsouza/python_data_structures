# Strings and Lists

a = "spam"
b = list(a)

# Converted string in a list
print("A string converted in a list:")
print(b)

# Spliting a string with spaces in a list
print("\nSplited string:")
a = "Asteca Peteca Discoteca"
b = a.split()
print(b)

# Spliting a string without spaces and a delimiter in a list
print("\nSplited string:")
a = "Asteca-Peteca-Discoteca"
b = a.split("-")
print(b)

# Joing strings with a delimiter
print("\nJoing strings with delimiter:")
delimiter = "-"
print(delimiter.join(b))