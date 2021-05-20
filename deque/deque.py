# DEQUE - Double-Ended Queue

class Deque:

    def __init__(self):
        self.deque = []
        self.len = 0

    def is_empty(self):
        if self.len == 0:
            return True
        return False

    def insert_front(self, element):
        # list_name.insert(index, element)
        self.deque.insert(0, element)
        self.len += 1

    def insert_back(self, element):
        # list_name.insert(index, element)
        self.deque.insert(self.len, element)
        self.len += 1

    def remove_front(self):
        self.deque.pop(0)
        self.len -= 1

    def remove_back(self):
        if not self.is_empty():
            self.deque.pop(self.len - 1)
            self.len -= 1
        return None

    def front(self):
        if not self.is_empty():
            return self.deque[0]
        return None

    def back(self):
        if not self.is_empty():
            return self.deque[-1]
        return None

    def show_deque(self):
        for i in self.deque:
            print(f"{i}", end=" ")
        print("\n")
        

d = Deque()

print(d.is_empty())

d.insert_front(10) # 10
d.insert_front(5)  # 5 10
d.insert_back(20) # 5 10 20
d.insert_front(7) # 7 5 10 20
d.insert_back(40) # 7 5 10 20 40

d.show_deque()

print(f"Front element: {d.front()}") # Print 7
print(f"Back element: {d.back()}\n") # Print 40

d.remove_back() # 7 5 10 20
d.show_deque()

d.remove_front() # 7 5 10 20
d.show_deque()

d.remove_back() # 7 5 10
d.show_deque()

d.remove_back() # 7 5
d.show_deque()

d.remove_back() # 7
d.show_deque()

d.remove_back() # empty
d.show_deque()