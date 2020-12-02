from grammar import Grammar
from grammar_menu import UI
from parserr import Parser


def read_pif(file_path):
    lst = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            elem = line.split("->")[0].strip()
            lst.append(elem)
    return lst


if __name__ == "__main__":
    # grammar = Grammar("g1.in")
    # ui = UI(grammar)
    # ui.run()

    lst = read_pif("p1.in")
    print(lst)

    parser = Parser()
    w = ["a", "a", "c", "b", "c"]
    parser.run(lst)
