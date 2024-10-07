from PIL import Image, ImageOps
import numpy as np


def text_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


height = 64

# Битмап исходного текста
with open("text.txt", "r") as f:
    text = f.read()

bit_text = list(map(int, text_to_bits(text)))
A = bit_text
c = 0

while len(A) % height > 0:
    A.append(0)
B = [[0] * height for i in range(len(A) // height)]
for i in range(len(A) // height):
    for j in range(height):
        B[i][j] = A[c]
        c += 1

text_bitmap = np.array(B) * 255
bmp_img1 = ImageOps.invert(Image.fromarray(np.uint8(text_bitmap), mode="L"))

# Битмап зашифрованного текста
with open("encrypted_text.txt", "r") as f:
    text = f.read()

bit_text = list(map(int, text_to_bits(text)))
A = bit_text
c = 0

while len(A) % height > 0:
    A.append(0)

B = [[0] * height for i in range(len(A) // height)]
for i in range(len(A) // height):
    for j in range(height):
        B[i][j] = A[c]
        c += 1

encrypted_text_bitmap = np.array(B) * 255
bmp_img2 = ImageOps.invert(Image.fromarray(
    np.uint8(encrypted_text_bitmap), mode="L"))
