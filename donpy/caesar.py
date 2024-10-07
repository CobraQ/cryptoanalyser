def encode_caesar(s, key):
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    key = 3
    subst = dict(zip(alphabet, alphabet[key:] + alphabet[:key]))
    res = "".join(map(subst.__getitem__, s))
    return res
