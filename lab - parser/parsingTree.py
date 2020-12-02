from typing import List

from configuration import *


class Node:
    def __init__(self, elem):
        self.element = elem
        self.parent = None
        self.left_child = None
        self.right_sibling = None


class ParserTree:
    def __init__(self, grammar):
        self.head = None
        self.grammar = grammar

    def create_tree(self, production_string: List[WorkElement]):
        if not production_string:
            return

        head = Node(production_string[0])
        self.head = head

        self.parse_node(head, production_string, 1)

        self.traverse_tree(head)

    def parse_node(self, node, production_string, index):
        production = self.grammar.productions[production_string[index - 1].value][
            production_string[index - 1].production_nr - 1]

        new_node = Node(WorkElement(production[0]))
        node.left_child = new_node
        node = node.left_child

        if index < len(production_string) and node.element.value == production_string[index].value:
            node.element.production_nr = production_string[index].production_nr
            index += 1
            self.parse_node(node, production_string, index)

        for i in range(1, len(production)):
            new_node = Node(WorkElement(production[i]))
            node.right_sibling = new_node
            node = node.right_sibling

            if index < len(production_string) and node.element.value == production_string[index].value:
                node.element.production_nr = production_string[index].production_nr
                index += 1
                self.parse_node(node, production_string, index)

    def print_node(self, node: Node):
        queue = []
        print(node.element.value)

        if node.left_child != None:
            queue.append(node.left_child)

        aux = node

        while aux.right_sibling != None:
            aux = aux.right_sibling
            print(' ' + str(aux.element.value), end=" ")
            if aux.left_child != None:
                queue.append(aux)

        print()

        if node.left_child != None:
            print("Left child: " + node.left_child.element.value)

        print()

        while queue:
            self.print_node(queue.pop(0))

    def traverse_tree(self, root):
        if root == None:
            return

        while root:
            print(f"{str(root.element)} ", end="")
            if root.left_child:
                self.traverse_tree(root.left_child)
            root = root.right_sibling
