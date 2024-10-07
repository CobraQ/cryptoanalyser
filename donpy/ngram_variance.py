import math


def count_ngrams(text, n):
    ngrams = {}
    for i in range(len(text) - n + 1):
        gram = text[i : i + n]
        if gram in ngrams:
            ngrams[gram] += 1
        else:
            ngrams[gram] = 1
    return ngrams


def calc_variance(ngrams):
    values = list(ngrams.values())
    mean = sum(values) / len(values)
    variance = sum([((x - mean) ** 2) for x in values]) / len(values)
    return variance
