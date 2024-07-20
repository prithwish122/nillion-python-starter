from nada_dsl import *

def add(a,b,c):
    sequence: list[SecretInteger] = []
    sequence.append(a)
    sequence.append(b)
    sequence.append(c)
    return sequence[0]+sequence[1]/sequence[2]


def nada_main():
    party1 = Party(name="Party1")
    # party2 = Party(name="Party2")
    # party3 = Party(name="Party3")
    a = SecretInteger(Input(name="a", party=party1))
    b = SecretInteger(Input(name="b", party=party1))
    c = SecretInteger(Input(name="c", party=party1))

    result = add(a,b,c)

    return [Output(result, "my_output", party1)]