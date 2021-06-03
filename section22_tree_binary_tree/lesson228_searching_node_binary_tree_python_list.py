# Searching for a Node in Binary Tree - Python List

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
    
new_bt = BinaryTree(8)
print(new_bt.insert_node("Drinks"))
print(new_bt.insert_node("Hot"))
print(new_bt.insert_node("Cold"))

# There's no Tea value
print(new_bt.search_node("Tea"))
print(new_bt.search_node("Hot"))