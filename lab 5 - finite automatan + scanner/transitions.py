class Transitions:
    def __init__(self):
        self.dict = {}

    def add_transition(self, start, end, value):
        if start in self.dict.keys():
            self.dict[start].append((end, value))
        else:
            self.dict[start] = [(end, value)]

    def get_transitions_with_start(self,start):
        if start not in self.dict.keys():
            return []
        return self.dict[start]

    def __str__(self):
        res = ""
        for start in self.dict.keys():
            for trans in self.dict[start]:
                str = start + " -> " + trans[1] + " -> " + trans[0] + "\n"
                res += str
        return res
