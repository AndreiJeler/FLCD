from grammar import Grammar
from configuration import *
from parsingTree import ParserTree


class Parser:
    def __init__(self):
        self.__grammar = Grammar("g3.in")
        self.__configuration = Configuration(self.__grammar.start)
        self.__parser_output = ParserTree(self.__grammar)

    def expand(self):
        nonterminal = self.__configuration.input_stack.pop(0)

        first_production = self.__grammar.productions[nonterminal][0]

        work_elem = WorkElement(nonterminal, 1)

        # self.__configuration.work_stack.append(nonterminal + "#1")
        self.__configuration.work_stack.append(work_elem)

        self.__configuration.input_stack = first_production + \
            self.__configuration.input_stack

    def advance(self):
        self.__configuration.index += 1
        terminal = self.__configuration.input_stack.pop(0)
        elem = WorkElement(terminal)
        self.__configuration.work_stack.append(elem)

    def momentary_insucces(self):
        self.__configuration.state = State.BACK

    def back(self):
        self.__configuration.index -= 1
        top_work_stack = self.__configuration.work_stack.pop(-1)
        self.__configuration.input_stack.insert(0, top_work_stack.value)

    def another_try(self):
        top_work_stack = self.__configuration.work_stack.pop(-1)
        # (non_terminal, production_nr) = top_work_stack.split("#")
        non_terminal = top_work_stack.value
        production_nr = top_work_stack.production_nr

        production_nr = int(production_nr)

        productions = self.__grammar.productions[non_terminal]

        current_production = productions[production_nr - 1]

        if production_nr != len(productions):
            next_production = productions[production_nr]

            self.__configuration.state = State.NORMAL
            self.__configuration.input_stack = self.__configuration.input_stack[len(
                current_production):]

            next_ind = production_nr + 1

            # self.__configuration.work_stack.append(
            #     non_terminal + "#" + str(next_ind))

            self.__configuration.work_stack.append(
                WorkElement(non_terminal, next_ind))

            self.__configuration.input_stack = next_production + \
                self.__configuration.input_stack

        elif self.__configuration.index == 1 and non_terminal == self.__grammar.start:
            self.__configuration.state = State.ERROR

        else:
            self.__configuration.input_stack[:] = self.__configuration.input_stack[len(
                current_production):]

            # self.__configuration.input_stack.insert(
            #     0, top_work_stack.split("#")[0])
            self.__configuration.input_stack.insert(0, non_terminal)

    def success(self):
        self.__configuration.state = State.FINAL

    def run(self, w):
        while self.__configuration.state != State.FINAL and self.__configuration.state != State.ERROR:
            print(self.__configuration)

            if self.__configuration.state == State.NORMAL:
                if not self.__configuration.input_stack and self.__configuration.index == len(w) + 1:
                    self.success()
                else:
                    if len(self.__configuration.input_stack) > 0 and self.__configuration.input_stack[
                            0] in self.__grammar.nonterminals:
                        self.expand()
                    else:
                        if len(self.__configuration.input_stack) > 0 and self.__configuration.index <= len(w) and \
                            self.__configuration.input_stack[0] == w[
                                self.__configuration.index - 1]:
                            self.advance()
                        else:
                            self.momentary_insucces()
            else:
                if self.__configuration.state == State.BACK:
                    if self.__configuration.work_stack[-1].value in self.__grammar.terminals:
                        self.back()
                    else:
                        self.another_try()

        if self.__configuration.state == State.ERROR:
            print("EROARE")
        else:
            print("Secventa este acceptata")
            print("final configuration: " + str(self.__configuration))
            production = []
            for elem in self.__configuration.work_stack:
                if elem.production_nr != 0:
                    production.append(elem)
            print("Production string:" +
                  str(['{0}'.format(element) for element in production]))
            self.__parser_output.create_tree(production)
