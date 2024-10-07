from itertools import cycle

alp = "abcdefghijklmnopqrstuvwxyz"


def encode_vijn(text, keytext):
    f = lambda arg: alp[(alp.index(arg[0]) + alp.index(arg[1]) % 26) % 26]
    return "".join(map(f, zip(text, cycle(keytext))))


def decode_vijn(coded_text, keytext):
    f = lambda arg: alp[alp.index(arg[0]) - alp.index(arg[1]) % 26]
    return "".join(map(f, zip(coded_text, cycle(keytext))))
