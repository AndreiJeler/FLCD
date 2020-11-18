from grammar import Grammar


class UI:
    def __init__(self, grammar):
        self.__grammar = grammar

    @staticmethod
    def print_menu():
        print("1. Print terminals")
        print("2. Print non-terminals")
        print("3. Print productions")
        print("4. Print starting symbol")

    def print_productions(self):
        productions = "Productions:\n"
        for prod in self.__grammar.productions.keys():
            productions += prod + " -> "
            for val in self.__grammar.productions[prod]:
                productions += str(val) + ' | '
            productions = productions[:-2]
            productions += '\n'
        print(productions)

    def print_terminals(self):
        terminals = "Terminals: "
        for terminal in self.__grammar.terminals:
            terminals += terminal + " "

        print(terminals)

    def print_nonterminals(self):
        nonterminals = "Nonterminals: "
        for nonterminal in self.__grammar.nonterminals:
            nonterminals += nonterminal + " "

        print(nonterminals)

    def print_starting_symbol(self):
        print(f"Starting symbol: {self.__grammar.start}")

    def run(self):
        while True:
            UI.print_menu()
            opt = int(input(">"))
            if opt == 1:
                self.print_terminals()
            elif opt == 2:
                self.print_nonterminals()
            elif opt == 3:
                self.print_productions()
            elif opt == 4:
                self.print_starting_symbol()
            else:
                return
