from pydes2.pyDes import *
from copy import copy


# The pydes library uses bytes all the time, but we like it better to work with
# integers, so we need to convert between the formats.
def int2byte(block):
    result = ""
    for b in block:
        result += chr(b)
    return result

def byte2int(block):
    return [ord(b) for b in block]

# Make a xor function that can handle lists of integers
def xor(a, b):
    return [a[i] ^ b[i] for i in range(0, 8)]

# Print what we are doing (msg) and then print out the blocks
# as uppercase hex thingy
def print_l(msg, l):
    print(msg)
    for block in l:
        print("".join(["%0.2X" % c for c in block]))

# Function to simulate the transmission error
def shift(old_cipher, dont_shift=False):
    new_cipher = copy(old_cipher)
    if dont_shift == False:
        new_cipher[0][0] = new_cipher[0][0] ^ 0x80
    print_l("Shifting", new_cipher)
    return new_cipher

# Encrypt a single block using the pydes library
def des_encrypt(message_block, key):
    algothingy = des(int2byte(key))
    cipher_block = algothingy.encrypt(int2byte(message_block))
    return byte2int(cipher_block)

# Decrypt a single block using the pydes library
def des_decrypt(cipher_block, key):
    algothingy = des(int2byte(key))
    message_block = algothingy.decrypt(int2byte(cipher_block))
    return byte2int(message_block)
