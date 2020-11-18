from grammar import Grammar
from grammar_menu import UI


if __name__ == "__main__":
    grammar = Grammar("g1.in")
    ui = UI(grammar)
    ui.run()
