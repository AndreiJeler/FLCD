from state import State


class WorkElement:
    def __init__(self, val, production_nr=0):
        self.value = val
        self.production_nr = production_nr

    def __str__(self):
        if self.production_nr == 0:
            return str(self.value)
        else:
            return str(self.value) + "#" + str(self.production_nr)


class Configuration:
    def __init__(self, starting_symbol):
        self.state = State.NORMAL
        self.index = 1
        self.work_stack = []
        self.input_stack = [starting_symbol]

    def __str__(self):
        work_stack_str = "["
        for elem in self.work_stack:
            work_stack_str += str(elem) +" ,"
        work_stack_str = work_stack_str[:-2]
        work_stack_str += "]"

        return "(" + self.state + " ," + str(self.index) + " , " + work_stack_str + " , " + str(
            self.input_stack) + ")"
