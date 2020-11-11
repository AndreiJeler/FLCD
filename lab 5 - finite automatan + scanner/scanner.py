from FiniteAutomata import FiniteAutomatan
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
        self._identifier_FA = FiniteAutomatan("identifier.in")
        self._integer_FA = FiniteAutomatan("integer.in")
        self._string_FA = FiniteAutomatan("string.in")
        self._string_FA.delta.add_transition("Q2","Q2"," ")

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
        # if i - 1 > 0 and not self.is_contained_in_operator(line[i-1]):
        #     return line[i], i+1
        # if line[i] == '+' or line[i] == '-' or line[i] == '=' or line[i] == '*' or line[i] == '\\':
        #     if i - 1 > 0 and line[i-1] not in self._separators and self.get_operator(line, i-1)[0] \
        #             and line[i+1] not in self._separators and not self.is_identifier(line[i+1]) and not self.is_constant(line[i+1]):
        #         return line[i], i + 1
        #     elif i-1 > 0 and self.is_identifier(line[i-1]) and self.is_identifier(line[i+1]) or self.is_constant(line[i+1]) or line[i+1] not in self._separators:
        #         return line[i], i + 1

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
        with open(self._file_name, "r", encoding="utf-8") as file:
            line_nr = 1
            ok = True
            for line in file:
                tokens = self.get_tokens_from_line(line)
                print(tokens)
                for token in tokens:
                    if token == ' ' or token == '\n':
                        continue
                    if token in self._separators or token in self._operators or token in self._reserved_words:
                        self._pif.add(token, -1)

                    elif self.is_identifier(token):
                        id = self._st.insert(token)
                        self._pif.add('identifier', id)

                    elif self.is_constant(token):
                        id = self._st.insert(token)
                        self._pif.add('constant', id)

                    else:
                        # raise Exception("Invalid token " + token + " at line" + str(line_nr))
                        print('\033[93m' + "Invalid token " + token + " at line" + str(line_nr) + '\033[0m')
                        ok = False

                line_nr += 1

        if ok:
            print("lexically correct")
            print(self._pif)
            self._pif.print_to_file()

            self._st.print()
            self._st.print_to_file()
        else:
            print("lexically incorrect. PIF and ST will not be printed.")

    def is_identifier(self, token):
        return self._identifier_FA.is_accepted(token)

    def is_constant(self, token):
        is_integer = self._integer_FA.is_accepted(token)
        is_string = self._string_FA.is_accepted(token)
        is_bool = token == True or token == False

        return is_integer or is_string or is_bool
