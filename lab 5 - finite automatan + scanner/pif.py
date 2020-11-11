class PIF:
    def __init__(self):
        self._pif = []

    def add(self, code, position):
        self._pif.append((code, position))

    def __str__(self):
        text = "PIF:\n"
        for elem in self._pif:
            text += str(elem[0]) + " -> " + str(elem[1]) + "\n"
        return text


    def print_to_file(self):
        with open("pif.out", 'w') as file:
            file.write(self.__str__())