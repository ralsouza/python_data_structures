# Inserting Data into Binary Tree

class BinaryTree:

    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full."
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "The value has been sucessfully inserted."
    
new_bt = BinaryTree(8)

print(new_bt.insert_node("Drinks")) # Root node
print(new_bt.insert_node("Hot")) # Left child
print(new_bt.insert_node("Cold")) # Right child