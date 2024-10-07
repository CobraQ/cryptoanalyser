import string


def generate_playfair_table(key):
    # Удалить все пробелы из ключа и привести к верхнему регистру
    key = str(key).replace(" ", "").upper()

    # Создать таблицу, начиная с букв A - Z
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = ""
    for letter in alphabet:
        if letter not in key:
            table += letter

    # Добавить буквы из ключа в таблицу
    for letter in key:
        if letter not in table:
            table += letter

    return table


def prepare_message(message):
    # Удалить все пробелы из сообщения и привести к верхнему регистру
    message = str(message).replace(" ", "").upper()

    # Заменить букву J на I
    message = message.replace("J", "I")

    # Убрать знаки препинания
    message = message.translate(str.maketrans("", "", string.punctuation))

    # Добавить X в конец, если длина сообщения нечетная
    if len(message) % 2 != 0:
        message += "X"

    return message


def find_coordinates(table, letter):
    # Найти координаты буквы в таблице
    row = 0
    col = 0
    index = table.index(letter)
    row = index // 5
    col = index % 5

    return (row, col)


def playfair_encrypt(plaintext, key):
    # Сгенерировать таблицу шифра Плейфера из ключа
    table = generate_playfair_table(key)

    # Подготовить сообщение для шифрования
    plaintext = prepare_message(plaintext)

    # Зашифровать сообщение
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        # Найти координаты двух букв из пары
        row1, col1 = find_coordinates(table, plaintext[i])
        row2, col2 = find_coordinates(table, plaintext[i + 1])

        # Зашифровать пару букв
        if row1 == row2:
            # Если буквы находятся в одной строке, то заменить их буквами в той же строке, но справа от них
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            # Если буквы находятся в одном столбце, то заменить их буквами в том же столбце, но ниже от них
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else:
            # Если буквы находятся в разных строках и столбцах, то заменить их буквами, находящимися на пересечении
            # строк первой буквы и столбца второй буквы, и наоборот
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]

    return ciphertext
