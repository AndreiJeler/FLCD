from pif import PIF
from symboltable import SymbolTable
from tokens import *
import re


class Scanner:
    def __init__(self, file):
        self._st = SymbolTable()
        self._pif = PIF()
        self._tokens = get_tokens()
        self._file_name = file
        self._separators = separators
        self._operators = operators
        self._reserved_words = reserved_words

    def get_string_constant(self, line, start_position):
        string = ''
        quote_count = 0
        i = start_position
        while i < len(line) and quote_count != 2:
            if line[i] == '"':
                quote_count += 1
            string += line[i]
            i += 1
        return string, i

    def is_contained_in_operator(self, token):
        for operator in operators:
            if token in operator:
                return True
        return False

    def get_operator(self, line, start_position):
        i = start_position
        token = ""
        while i < len(line) and line[i] not in operators and self.is_contained_in_operator(line[i]):
            token += line[i]
            i += 1
        if token in operators:
            return token, i
        return None, start_position

    def get_tokens_from_line(self, line):
        token = ""
        index = 0
        tokens = []

        while index < len(line):
            if line[index] == '"':
                if token:
                    tokens.append(token)
                token, index = self.get_string_constant(line, index)
                tokens.append(token)
                token = ""

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token = ""
                tokens.append(line[index])
                index += 1

            elif self.is_contained_in_operator(line[index]):
                operator, index = self.get_operator(line, index)
                if operator != None:
                    if token:
                        tokens.append(token)
                    tokens.append(operator)
                    token = ""
                else:
                    token += line[index]
                    index += 1

            else:
                token += line[index]
                index += 1

        if token:
            tokens.append(token)

        return tokens

    def run(self):
        with open(self._file_name, "r") as file:
            line_nr = 1
            for line in file:
                tokens = self.get_tokens_from_line(line)
                print(tokens)
                for token in tokens:
                    if token in self._separators or token in self._operators or token in self._reserved_words:
                        self._pif.add(self._tokens[token], -1)

                    elif self.is_identifier(token):
                        id = self._st.insert(token)
                        self._pif.add(self._tokens['identifier'], id)

                    elif self.is_constant(token):
                        id = self._st.insert(token)
                        self._pif.add(self._tokens['constant'], id)

                    else:
                        raise Exception("Invalid token " + token + " at line" + str(line_nr))

                line_nr += 1

        print(self._pif)
        print(self._st.print())

    def is_identifier(self, token):
        return re.match('^[a-zA-Z_]([a-zA-Z0-9]){,255}$', token) is not None

    def is_constant(self, token):
        # return re.match('^[a-zA-Z_]([a-zA-Z0-9]){,255}$', token) is not None
        return True
