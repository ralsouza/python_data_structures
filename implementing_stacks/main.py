
class Stack:
    def __init__(self):
        self.stack = []

    # Appending an element at the end.
    def push(self, element):
        self.stack.append(element)
        print(f"Element {element} is added.")
        return None

    # Removing the last element
    def pop(self):
        if not self.empty():
            self.stack.pop(len(self.stack) -1)
            print("The last element is removed.")
            return None
        print("The list is empty.")
        return None

    # Selecting the top element
    def top(self):
        print(f"The top element is {self.stack[-1]}")
        return None

    # Checking whether the list are empty
    def empty(self):
        if (len(self.stack) == 0):
            return True
        return False

if __name__ == "__main__":
    
    s = Stack()

    print(s.empty())

    s.push(1)
    s.push(2)
    s.push(3)

    s.top()
    print(s.empty())

    s.pop()
    s.top()
