# NEPTUN1 NEPTUN2

def avg(ls: list) -> int:
    if len(ls) != 0:
        return sum(ls) / len(ls)
    else:
        return 0


def decision(h1: list, h2: list) -> int:
    if avg(h2[:4]) >= 0.5:
        return 1
    else:
        return 0
