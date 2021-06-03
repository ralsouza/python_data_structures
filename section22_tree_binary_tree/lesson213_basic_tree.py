# Basic Tree

class TreeNode:

    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, TreeNode):
        self.children.append(TreeNode)
    

tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])

tree.add_child(cold)
tree.add_child(hot)

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])

hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(cola)
cold.add_child(fanta)

print(tree)