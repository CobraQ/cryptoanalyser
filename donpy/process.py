import string
from vijn import encode_vijn
#from aes import encrypt_aes
from caesar import encode_caesar
from playfair import playfair_encrypt

from byte_entropy import byte_entropy
from ngram_variance import calc_variance
from ngram_variance import count_ngrams


def process(choosen_key, choosen_cypher_i):
    with open("text.txt", "r") as f:
        text = f.read()

    print(byte_entropy(text))
    if choosen_cypher_i == 0:  # Выбран виженер
        text = text.lower()
        text = text.replace(" ", "")
        text = text.translate(str.maketrans("", "", string.punctuation))
        encrypted_text = encode_vijn(text, choosen_key)
        with open("encrypted_text.txt", "w") as f_enc:
            f_enc.write(encrypted_text)

        print(text + " > " + encrypted_text)
        print(byte_entropy(encrypted_text) - byte_entropy(text))

    if choosen_cypher_i == 1:  # Выбран AES-256
        encrypted_text = encrypt_aes(text, choosen_key)
        with open("encrypted_text.txt", "w") as f_enc:
            f_enc.write(encrypted_text)

        print(text + " > " + encrypted_text)
        print(byte_entropy(encrypted_text) - byte_entropy(text))

    if choosen_cypher_i == 2:  # Выбран Цезарь
        text = text.lower()
        text = text.replace(" ", "")
        text = text.translate(str.maketrans("", "", string.punctuation))
        encrypted_text = encode_caesar(text, choosen_key)
        with open("encrypted_text.txt", "w") as f_enc:
            f_enc.write(encrypted_text)

        print(text + " > " + encrypted_text)
        print(byte_entropy(encrypted_text) - byte_entropy(text))

    if choosen_cypher_i == 3:  # Выбран Плейфер
        encrypted_text = playfair_encrypt(text, choosen_key)
        with open("encrypted_text.txt", "w") as f_enc:
            f_enc.write(encrypted_text)

        print(text + " > " + encrypted_text)
        print(byte_entropy(encrypted_text) - byte_entropy(text))

    if choosen_cypher_i == 4:  # Выбрано вычисление из файла
        with open("encrypted_text.txt", "r") as f_enc:
            encrypted_text = f_enc.read()

    bigrams = count_ngrams(text, 2)
    trigrams = count_ngrams(text, 3)
    print("Full Text Variance:", calc_variance(bigrams | trigrams))
    enc_bigrams = count_ngrams(encrypted_text, 2)
    enc_trigrams = count_ngrams(encrypted_text, 3)
    print("Full Encoded Text Variance:", calc_variance(enc_bigrams | enc_trigrams))

    result = (
        "Рост энтропии: "
        + str(round((byte_entropy(encrypted_text) - byte_entropy(text)) * 100, 4))
        + " %"
        + "\n"
        + "Дисперсия N-грамм исходного текста: "
        + str(round(calc_variance(bigrams | trigrams), 4))
        + "\n"
        + "Дисперсия N-грамм шифротекста: "
        + str(round(calc_variance(enc_bigrams | enc_trigrams), 4))
    )
    return result
