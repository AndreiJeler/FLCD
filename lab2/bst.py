from node import *


class BinarySearchTree:
    def __init__(self):
        self.current_position = 1
        self.root = None

    def insert(self, identifier):
        new_node = Node(identifier)

        if self.root is None:
            self.root = new_node
            new_node.position = self.current_position
            self.current_position += 1

        node = NodeOperations.search(self.root, identifier)
        if node:
            return node.position

        NodeOperations.insert(self.root, new_node)
        new_node.position = self.current_position
        self.current_position += 1

    def print_BST(self):
        NodeOperations.inorder(self.root)
