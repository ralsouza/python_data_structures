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

    