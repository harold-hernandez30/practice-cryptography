

from parse_text import read_input
from string import ascii_uppercase
from collections import OrderedDict
from alpha_count import alpha_count

def decrypt(input_ciphertext):
    filename = "sample/moby.txt"
    book = read_input(filename)

    mobydick_alpha_count = alpha_count(book)

    print(f"Moby Dick: {mobydick_alpha_count}")

    print(f"Input Ciphertext: {alpha_count(input_ciphertext)}")