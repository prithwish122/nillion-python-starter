from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    # party2 = Party(name="Party2")
    # party3 = Party(name="Party3")
    a = SecretInteger(Input(name="a", party=party1))
    b = SecretInteger(Input(name="b", party=party1))
    c = SecretInteger(Input(name="c", party=party1))

    result = a * b * c

    return [Output(result, "my_output", party1)]