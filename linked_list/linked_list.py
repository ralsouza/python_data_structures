class Node:

    def __ini__(self, label):
        self.label = label
        self.next = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.set_next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):

        if index >= 0:
            # Creating a new node
            node = Node(label)

            # Checking whether list is empty
            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    # Inserting at begining
                    node.set_next(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserting at the end
                    node.set_next(self.last)
                    self.last = node
                else:
                    # Insert in the middle
                    prev_node = self.first
                    curr_node = self.first.get_next()
                    curr_index = 1

                    while curr_node != None:
                        if curr_index == index:
                            # Sets the curr_node as next node
                            node.set_next(curr_node)

                            # Sets the node as next of the prev_node
                            prev_node.set_next(node)
                            
                            break

                        prev_node = curr_node
                        curr_node = curr_node.get_next()
                        curr_index += 1

            # Refresh list size
            self.len_list += 1

    def pop(self, index):
        
        if not self.empty() and index >= 0 and index < self.len_list:

            flag_remove = False

            if self.first.get_next() == None:
                # Having only one element
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # Removing from the begining, but has more than one element
                self.first = self.first.get_next()
                flag_remove = True
            else:
                """
                    The list has more than one element and the remove isn't 
                    at the begining
                """
                prev_node = self.first
                curr_node = self.first.get_next()
                curr_index += 1

                while curr_node != None:
                    if index == curr_index:
                        # The next of the previous points to the next current node
                        prev_node.set_next(curr_node.get_next())
                        curr_node.set_next(None)
                        flag_remove = True
                        break

                    prev_node = curr_node
                    curr_node = curr_node.get_next()
                    curr_index += 1

            if flag_remove:
                self.len_list -= 1
