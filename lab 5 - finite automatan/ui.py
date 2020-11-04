from FiniteAutomata import *


class UI:
    def __init__(self, fa: FiniteAutomatan):
        self.finite_automata = fa

    def print_menu(self):
        print("1)Get the list of states")
        print("2)Get the alphabet")
        print("3)Get the initial state")
        print("4)Get the final states")
        print("5)Get the list of transactions")
        print("6)Is deterministic")
        print("7)Is accepted")

    def ui_is_deterministic(self):
        res = self.finite_automata.is_deterministic()
        if res:
            print("The FA is deterministic")
        else:
            print("The Fa is not deterministic")

    def ui_is_accepted(self):
        text = input("Enter the word to check: ")
        res = self.finite_automata.is_accepted(text)
        if res:
            print("The string " + text + " is accepted")
        else:
            print("The string " + text + " is not accepted")

    def run(self):
        options = {1: self.finite_automata.print_states, 2: self.finite_automata.print_alphabet,
                   3: self.finite_automata.print_initial_state, 4: self.finite_automata.print_final_states,
                   5: self.finite_automata.print_transitions, 6: self.ui_is_deterministic, 7: self.ui_is_accepted}
        while True:
            self.print_menu()
            try:
                opt = int(input(">>"))
                if opt not in range(1, 8):
                    return
                options[opt]()
                print()
            except Exception as ex:
                print(ex)
                return
