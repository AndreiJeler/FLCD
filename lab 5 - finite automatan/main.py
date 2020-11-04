from FiniteAutomata import *
from ui import UI


def test():
    fa = FiniteAutomatan("fa.in")
    assert fa.is_deterministic() == True
    assert fa.is_accepted("aac") == True
    assert fa.is_accepted("aba") == False
    assert fa.is_accepted("aaaaaaab") == True
    assert fa.is_accepted("aaaa") == False

    non_det = FiniteAutomatan("nonDet.in")
    assert non_det.is_deterministic() == False


if __name__ == '__main__':
    test()
    fa = FiniteAutomatan("fa.in")
    ui = UI(fa)
    ui.run()
