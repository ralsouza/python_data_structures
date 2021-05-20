class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    # Insert at end
    def insert(self, element):
        self.queue.append(element)
        self.len_queue += 1

    # Remove at the begining, First in First out (FIFO)
    def remove(self):
        if not self.is_empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def is_empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length_queue(self):
        return self.len_queue

    def first_element(self):
        if not self.is_empty():
            return self.queue[0]
        print("There aren't element in the queue.")
        return None

    def print_queue(self):
        print()

q = Queue()

print(q.is_empty())

q.insert(1)
q.insert(2)
q.insert(3)

q.remove() # Remove the fist element, 1
q.remove()
q.remove()

print(q.first_element())

