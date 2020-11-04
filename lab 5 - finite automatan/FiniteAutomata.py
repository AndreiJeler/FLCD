from transitions import Transitions


class FiniteAutomatan:
    def __init__(self, file_name):
        self.file_name = file_name
        self.Q = set()
        self.E = set()
        self.q0 = None
        self.F = set()
        self.delta = Transitions()
        self.read_file()

    def read_file(self):
        with open(self.file_name, 'r') as file:
            self.Q = file.readline().strip('\n').split(' ')
            self.E = file.readline().strip('\n').split(' ')
            self.q0 = file.readline().strip('\n')
            self.F = file.readline().strip('\n').split(' ')
            line = file.readline().strip('\n')
            while line:
                line = line.split(' ')
                for i in range(2, len(line)):
                    self.delta.add_transition(line[0], line[1], line[i])
                line = file.readline().strip('\n')

    def print_states(self):
        print("List of states:")
        for state in self.Q:
            print(state)

    def print_alphabet(self):
        print("The alphabet of the FA:")
        for val in self.E:
            print(val)

    def print_initial_state(self):
        print("The initial state of the FA: ", self.q0)

    def print_final_states(self):
        print("The list of final states:")
        for state in self.F:
            print(state)

    def print_transitions(self):
        print("The list of transitions:")
        print(self.delta)

    def is_deterministic(self):
        for state in self.Q:
            transitions = self.delta.get_transitions_with_start(state)
            for transition in transitions:
                unique_transitions = list(filter(lambda x: x[1] != transition[1], transitions))
                if len(unique_transitions) != len(transitions) - 1:
                    return False
        return True

    def is_accepted(self, string):
        if not self.is_deterministic():
            raise Exception("The FA is not deterministic")
        current_state = self.q0
        for i in range(len(string)):
            possible_transitions = self.delta.get_transitions_with_start(current_state)
            current_value = string[i]
            current_state = None
            for transition in possible_transitions:
                if transition[1] == current_value:
                    current_state = transition[0]
            if current_state is None:
                return False
        if current_state not in self.F:
            return False
        return True
