# 6th day of challenge


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, data):
        if data<self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
            self.left.parent = self
        elif data>self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
            self.left.parent = self
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

def get_path_to_root(start_node):
    if start_node.parent is None:
        return start_node
    result = get_path_to_root(start_node.parent)
    result = result + [start_node.data]
    return result

tree = Node(1)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(0)
print(get_path_to_root())


