from parse_text import read_input
from string import ascii_uppercase
from collections import OrderedDict
from alpha_count import alpha_count
from ceasar_cipher import decrypt

filename = "sample/moby.txt"
book = read_input(filename)

input_ciphertext = "OR FHER GB QEVAX LBHE BINYGVAR"

decrypt(input_ciphertext)


# R -> E
# O(E) FHE(E) GB QEVAX LBHE BINVYGVA(E)
# E -> E
# OR FHER GB QEVAX LBHE BINYGVAR (no changes)
# B -> E
# OR FHER G(E) QEVAX L(E)HE (E)INYGVAR 



