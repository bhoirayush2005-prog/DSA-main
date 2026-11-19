class node:
    def __init__(self,value):
        self.right=None
        self.data=value
        self.left=None
class binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
            return

        temp=self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left=new_node
                    return
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return
                temp=temp.right

    def search(self,key):
        temp=self.root
        while temp is not None:
            if key == temp.data:
                return temp
            if key < temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return None
