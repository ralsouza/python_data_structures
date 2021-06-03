# Create Binary Tree - Python List

class BinaryTree:

    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

new_bt = BinaryTree(8)

