from typing import List

from configuration import *


class Node:
    def __init__(self, elem, pos=0):
        self.element = elem
        self.parent = None
        self.left_child = None
        self.right_sibling = None
        self.position = pos

    def __str__(self):
        parent = self.parent.position if self.parent else None
        left_c = self.left_child.position if self.left_child else None
        right_s = self.right_sibling.position if self.right_sibling else None
        return f"Node: position {self.position} value: {str(self.element)} Parent {parent} Left_child: {left_c} Right_sibling {right_s}"



class ParserTree:
    def __init__(self, grammar):
        self.head = None
        self.table = {}
        self.values = []
        self.grammar = grammar
        self.current_position = 1
        self.current_index = 1

    def create_tree(self, production_string: List[WorkElement]):
        if not production_string:
            return

        head = Node(production_string[0], 0)
        self.head = head
        self.values.append(str(head.element))
        self.table[0] = head

        self.parse_node(head, production_string)

        with open("parser.out", 'w') as f:
            self.print_all(f)

        self.print_all()

    def parse_node(self, node, production_string):
        parent = node
        non_terminal = production_string[self.current_index-1].value
        production_nr = production_string[self.current_index-1].production_nr
        production = self.grammar.productions[non_terminal][
            production_nr - 1]

        new_node = Node(WorkElement(production[0]), self.current_position)
        node.left_child = new_node
        new_node.parent = parent
        node = node.left_child
        self.table[self.current_position] = new_node

        self.values.append(str(new_node.element))

        if self.current_index < len(production_string) and node.element.value == production_string[self.current_index].value:
            node.element.production_nr = production_string[self.current_index].production_nr
            self.current_index += 1
            self.current_position += 1
            self.parse_node(node, production_string)

        for i in range(1, len(production)):
            self.current_position += 1
            new_node = Node(WorkElement(production[i]), self.current_position)
            new_node.parent = parent
            self.table[self.current_position] = new_node
            node.right_sibling = new_node
            node = node.right_sibling
            self.values.append(str(new_node.element))

            if self.current_index < len(production_string) and node.element.value == production_string[self.current_index].value:
                node.element.production_nr = production_string[self.current_index].production_nr
                self.current_index += 1
                self.current_position += 1
                self.parse_node(node, production_string)

    def print_all(self, file=None):
        fathers = [-1 for _ in range(len(self.values))]
        left_child = [-1 for _ in range(len(self.values))]
        right_sibling = [-1 for _ in range(len(self.values))]
        to_print = ""
        for node in self.table.values():
            if node.parent:
                fathers[node.position] = node.parent.position
            if node.left_child:
                left_child[node.position] = node.left_child.position
            if node.right_sibling:
                right_sibling[node.position] = node.right_sibling.position
            to_print = ""

            if node.position == 0:
                to_print += str(node.element)
            else:
                node_copy = node
                while node_copy.parent:
                    if node_copy.parent.right_sibling:
                        to_print = "|\t" + to_print
                    else:
                        to_print = "\t" + to_print
                    node_copy = node_copy.parent

                if node.right_sibling is None:
                    to_print += "\\--"
                else:
                    to_print += "|--"
                to_print += str(node.element)

            if file is None:
                print(to_print)
            else:
                file.write(to_print + "\n")

        if file is None:
            print(
                f' \nFathers: {fathers}\nLeft children: {left_child}\nRight siblings = {right_sibling}')
        else:
            file.write(
                f' \nFathers: {fathers}\nLeft children: {left_child}\nRight siblings = {right_sibling}')

        # for val in self.table.values():
        #     print(val)
