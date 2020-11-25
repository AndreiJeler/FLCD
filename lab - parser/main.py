from grammar import Grammar
from grammar_menu import UI
from parserr import Parser

if __name__ == "__main__":
    # grammar = Grammar("g1.in")
    # ui = UI(grammar)
    # ui.run()

    parser = Parser()
    parser.run("aacbc")
