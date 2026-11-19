
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    # Search for a value
    def search(self, key):
        temp = self.root

        while temp is not None:
            if key == temp.data:
                return temp

            elif key < temp.data:
                temp = temp.left

            else:
                temp = temp.right

        return None


# Main program
bst = BinarySearchTree()

bst.insert(Node(50))
bst.insert(Node(30))
bst.insert(Node(70))
bst.insert(Node(20))
bst.insert(Node(40))
bst.insert(Node(60))
bst.insert(Node(80))

result = bst.search(40)

if result:
    print("Element Found:", result.data)
else:
    print("Element Not Found")
