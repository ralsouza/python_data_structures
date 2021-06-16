# Deleting a node in Binary Search Tree

# Case 1: The node to be deleted is a leaf node
# Case 2: The node has one child
# Case 3: The node has two children

import QueueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert_node(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTNode(node_value)
        else:
            insert_node(root_node.right_child, node_value)
    return "The node has been successfully inserted."

def pre_order_traversal(root_node):
    if not root_node:
        return 
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)

def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)

def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)

def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(root_node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                customQueue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                customQueue.enqueue(root.value.right_child)

def search_node(root_node, node_value):
    if root_node.data == node_value:
        print("The value is found.")
    elif node_value < root_node.data:
        if root_node.left_child.data ==  node_value:
            print("The value is found.")
        else:
            search_node(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print("the value is found.")
        else:
            search_node(root_node.right_child, node_value)

# Find minimum node to be sucessor
def minimum_value_node(bst_node):
    current = bst_node
    while (current.left_child is not None):
        current = current.left_child 
    return current

def delete_node(root_node, node_value):
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp

        if root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp

        temp = minimum_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node


new_bst = BSTNode(None)

insert_node(new_bst, 70)
insert_node(new_bst, 50)
insert_node(new_bst, 90)
insert_node(new_bst, 30)
insert_node(new_bst, 60)
insert_node(new_bst, 80)
insert_node(new_bst, 100)
insert_node(new_bst, 20)
insert_node(new_bst, 40)

delete_node(new_bst, 100)
level_order_traversal(new_bst)


