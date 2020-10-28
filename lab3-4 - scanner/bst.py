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

        node = self.search(identifier)
        if node:
            return node.position

        NodeOperations.insert(self.root, new_node)
        new_node.position = self.current_position
        self.current_position += 1
        return new_node.position

    def print_BST(self):
        NodeOperations.inorder(self.root)

    def search(self, identifier):
        return NodeOperations.search(self.root, identifier)

    def print_to_file(self):
        NodeOperations.print_to_file(self.root)