from symboltable import *
from tokens import *
from scanner import *


def test_ST():
    st = SymbolTable()
    st.insert("e")
    st.insert("b")
    st.insert("c")
    st.insert("a")
    print(st.insert("e"))
    print(st.insert("c"))
    st.print()


if __name__ == '__main__':
    #test_ST()
    scanner = Scanner("p1err.in")
    scanner.run()
