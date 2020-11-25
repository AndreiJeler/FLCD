from state import State


class Configuration:
    def __init__(self, starting_symbol):
        self.state = State.NORMAL
        self.index = 0
        self.work_stack = []
        self.input_stack = [starting_symbol]
