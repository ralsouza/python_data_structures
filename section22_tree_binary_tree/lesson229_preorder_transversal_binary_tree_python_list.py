# PreOrder Transversal of Binary Tree - Python List
# Root Node > Left Subtree > Right Subtree

from typing import NewType


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
    
    def preorder_transversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.preorder_transversal(index*2)
        self.preorder_transversal(index*2+1)

new_bt = BinaryTree(8)

new_bt.insert_node("Drinks")
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")
new_bt.insert_node("Tea")
new_bt.insert_node("Coffee")

new_bt.preorder_transversal(1)