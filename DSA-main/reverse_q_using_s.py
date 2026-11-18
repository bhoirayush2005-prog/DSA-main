class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Element pushed successfully")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return

        removed = self.top
        self.top = self.top.next
        print("Popped element:", removed.data)

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return

        print("Top element:", self.top.data)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return

        current = self.top
        print("Stack elements:")
        while current is not None:
            print(current.data)
            current = current.next


stack = Stack()

while True:
    print("\n===== STACK USING LINKED LIST =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the element: "))
        stack.push(value)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")