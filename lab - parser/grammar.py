class Grammar:
    def __init__(self, file):
        self.__nonterminals = []
        self.__terminals = []
        self.__productions = {}
        self.__start = ""
        self.__file = file
        self.read_from_file()
        self.validate_production()
        self.validate_starting_symbol()

    def validate_starting_symbol(self):
        if self.start not in self.__nonterminals:
            raise Exception(
                f"Starting symbol {self.start} is not in the list of nonterminals")

    def validate_production(self):
        for nonterminal in self.__productions.keys():
            if nonterminal not in self.__nonterminals:
                raise Exception(
                    f"Lhs {nonterminal} is not in the list of nonterminals")

            for thing in self.__productions[nonterminal]:
                for thing2 in thing:
                    if thing2 not in self.__nonterminals and thing2 not in self.__terminals:
                        raise Exception(
                            f"{thing2} is not in the list of terminals/nonterminals")

    def read_from_file(self):
        with open(self.__file, "r") as filee:
            self.__nonterminals = filee.readline().strip().split(" ")
            self.__terminals = filee.readline().strip().split(" ")
            self.__start = filee.readline().strip()
            for line in filee.readlines():
                self.__productions[line.split(
                    "-")[0].strip()] = [val.strip().split(" ") for val in line.split("-")[1].strip().split("|")]
            print(self.__productions)

    @property
    def nonterminals(self):
        return self.__nonterminals

    @property
    def terminals(self):
        return self.__terminals

    @property
    def productions(self):
        return self.__productions

    @property
    def start(self):
        return self.__start
