from grammar import Grammar
from configuration import *


class Parser:
    def __init__(self):
        self.__grammar = Grammar("g1.in")
        self.__configuration = Configuration(self.__grammar.start)

    def expand(self):
        nonterminal = self.__configuration.input_stack.pop(0)
        # self.__configuration.work_stack.append(nonterminal)
        first_production = self.__grammar.productions[nonterminal][0]
        self.__configuration.work_stack.append(nonterminal + "#1")
        for i in range(len(first_production) - 1, -1, -1):
            self.__configuration.input_stack.insert(0, first_production[i])
        # self.__configuration.input_stack.insert(
        #     0, self.__grammar.productions[nonterminal][0])

    def advance(self):
        self.__configuration.index += 1
        terminal = self.__configuration.input_stack.pop(0)
        self.__configuration.work_stack.append(terminal)

    def momentary_insucces(self):
        self.__configuration.state = State.BACK

    def back(self):
        self.__configuration.index -= 1
        top_work_stack = self.__configuration.work_stack.pop(-1)
        self.__configuration.input_stack.insert(0, top_work_stack)

    def another_try(self):
        top_work_stack = self.__configuration.work_stack.pop(-1)
        productions = self.__grammar.productions[top_work_stack.split('#')[
            0]]
        next_production = productions[int(top_work_stack.split('#')[1])]
        current = productions[int(top_work_stack.split('#'), 0)]
        if next_production:
            self.__configuration.state = State.NORMAL
            for i in range(len(next_production)):
                self.__configuration.input_stack.pop(0)
            next_ind = int(top_work_stack.split('#')[1])+1
            self.__configuration.work_stack.append(
                top_work_stack.split('#')[0] + "#" + str(next_ind))
            for i in range(len(current) - 1, -1, -1):
                self.__configuration.input_stack.insert(0, current[i])
            # self.__configuration.input_stack = next_production[0] + \
            #    self.__configuration.input_stack
        elif self.__configuration.index == 0 and top_work_stack[0] == self.__grammar.start:
            self.__configuration.state = State.ERROR
        else:
            self.__configuration.input_stack.insert(
                0, top_work_stack.split("#")[0])

    def succes(self):
        self.__configuration.state = State.FINAL

    def run(self, w):
        while self.__configuration.state != State.FINAL and self.__configuration.state != State.ERROR:
            print(self.__configuration.work_stack)
            print(self.__configuration.input_stack)

            if self.__configuration.state == State.NORMAL:
                if not self.__configuration.input_stack and self.__configuration.index == len(w):
                    self.succes()
                else:
                    if self.__configuration.input_stack[0] in self.__grammar.nonterminals:
                        self.expand()
                    else:
                        if self.__configuration.input_stack[0] == w[self.__configuration.index]:
                            self.advance()
                        else:
                            self.momentary_insucces()
            else:
                if self.__configuration.state == State.BACK:
                    if self.__configuration.work_stack[0] in self.__grammar.terminals:
                        self.back()
                    else:
                        self.another_try()

        if self.__configuration.state == State.ERROR:
            print("EROARE")
        else:
            print("Secventa este acceptata")
