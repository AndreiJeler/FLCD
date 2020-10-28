def get_tokens():
    tokens = {}
    currentId = 0
    with open("tokens.in", 'r') as file:
        for line in file:
            line = line.strip("\n")
            token = line
            if token=="":
                token=" "
            tokens[token] = currentId
            currentId += 1
        tokens['\n'] = currentId
    return tokens


operators = ['+', '-', '*', '/', '%', '=', '<', '<=', '>', '>=', '==', '!=', 'and', 'or', 'not']
separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ',', '\n', '\t']
reserved_words = ['if', 'else', 'elif', 'while', 'for', 'read', 'write', 'integer', 'char', 'string', 'program', 'return']
