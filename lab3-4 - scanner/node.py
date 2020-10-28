class Node:
    def __init__(self, identifier=""):
        self.identifier = identifier
        self.position = 0
        self.left = None
        self.right = None


class NodeOperations:
    @staticmethod
    def insert(root: Node, node: Node):
        if root is None:
            root = node
        else:
            if root.identifier < node.identifier:
                if root.right is None:
                    root.right = node
                else:
                    NodeOperations.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    NodeOperations.insert(root.left, node)

    @staticmethod
    def search(root, identifier):
        if root is None:
            return None
        if root.identifier == identifier:
            return root
        if root.identifier > identifier:
            return NodeOperations.search(root.left, identifier)
        if root.identifier < identifier:
            return NodeOperations.search(root.right, identifier)
        return None

    @staticmethod
    def inorder(root):
        if root:
            NodeOperations.inorder(root.left)
            print(root.identifier + "->" + str(root.position))
            NodeOperations.inorder(root.right)

    @staticmethod
    def inorder_result(root, file):
        if root:
            NodeOperations.inorder_result(root.left, file)
            file.write(root.identifier + "->" + str(root.position) + '\n')
            NodeOperations.inorder_result(root.right, file)

    @staticmethod
    def print_to_file(root):
        with open("st.out", 'w') as file:
            NodeOperations.inorder_result(root, file)
