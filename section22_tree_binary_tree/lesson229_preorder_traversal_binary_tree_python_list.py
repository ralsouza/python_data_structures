# PreOrder Traversal of Binary Tree - Python List
# Root Node > Left Subtree > Right Subtree

class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full."
        self.custom_list[self.last_used_index+1] = value
        self.last_used_index += 1
        return "The value has been sucessfully inserted."

    def search_node(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Success."
        return "Not found."
    
    def pre_order_traversal(self, index):
        if index > self.last_used_index: # If true, we visited all nodes and stop the search
            return
        print(self.custom_list[index]) # Visit the root node
        self.pre_order_traversal(index*2) # Visit the left subtree
        self.pre_order_traversal(index*2+1) # Visit the right subtree

new_bt = BinaryTree(8)

new_bt.insert_node("Drinks") # Root node
new_bt.insert_node("Hot") # Left node
new_bt.insert_node("Cold") # Right node
new_bt.insert_node("Tea") # Left child of Hot node
new_bt.insert_node("Coffee") # Right child of Hot node

new_bt.pre_order_traversal(1) # First index is 1, because 0 index is empty in this case