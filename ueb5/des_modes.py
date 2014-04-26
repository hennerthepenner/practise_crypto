###
# Given the block cipher DES and key k = 0xFF0000000000000.
# Alice transmits four block with 64 bits of data each to Bob, but 
# unfortunately a transmission error occurs. Assume that all data blocks are 
# just zeros.
# Encrypt the data, then change the first bit in the first block and decrypt!
# What block are affected by the transmission errors and how?
###

from copy import copy
from utils import *


# Specify key and also use key as IV for some modes
key = [0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
iv = key

# Make four blocks with zeros only
data = [
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
]


###
# ECB is pretty simple. There is no IV involved, therefore all blocks are 
# encrypted and decrypted without affecting the other blocks. The transmission 
# has consequences only for the first block.
#
# For encryption:
# c0 = enc(m0, key)
# c1 = enc(m1, key)
# c2 = enc(m2, key)
#
# For decryption:
# m0 = dec(c0, key)
# m1 = dec(c1, key)
# m2 = dec(c2, key)
###

def ecb_encrypt(message):
    cipher = [des_encrypt(block, key) for block in message]
    print_l("ECB encryption", cipher)
    return cipher

def ecb_decrypt(cipher):
    message = [des_decrypt(block, key) for block in cipher]
    print_l("ECB decryption", message)
    return message

def ecb():
    original_cipher = ecb_encrypt(data)
    changed_cipher = shift(original_cipher)
    message = ecb_decrypt(changed_cipher)


###
# In CBC the transmission error scrambles the block it occurs in and also 
# produces a 1 bit error in the following block.
#
# For encryption:
# c0 = enc(xor(m0, IV), key)
# c1 = enc(xor(m1, c0), key)
# c2 = enc(xor(m2, c1), key)
#
# For decryption:
# m0 = xor(dec(c0, key), IV)
# m1 = xor(dec(c1, key), c0)
# m2 = xor(dec(c2, key), c1)
###

def cbc_encrypt(message):
    cipher = []
    cbc_iv = copy(iv)
    for message_block in message:
        cipher_block = des_encrypt(xor(cbc_iv, message_block), key)
        cipher.append(cipher_block)
        cbc_iv = cipher_block
    print_l("CBC encryption", cipher)
    return cipher

def cbc_decrypt(cipher):
    message = []
    cbc_iv = copy(iv)
    for cipher_block in cipher:
        message_block = des_decrypt(cipher_block, key)
        message.append(xor(message_block, cbc_iv))
        cbc_iv = cipher_block
    print_l("CBC decryption", message)
    return message

def cbc():
    original_cipher = cbc_encrypt(data)
    changed_cipher = shift(original_cipher, dont_shift=False)
    message = cbc_decrypt(changed_cipher)


###
# In CFB the transmission error scrambles the block following the block the 
# error occured in, but also gives a 1 bit error in the block it occured in.
#
# For encryption:
# c0 = xor(enc(IV, key), m0)
# c1 = xor(enc(c0, key), m1)
# c2 = xor(enc(c1, key), m2)
#
# For decryption:
# m0 = xor(enc(IV, key), c0)
# m1 = xor(enc(c0, key), c1)
# m2 = xor(enc(c1, key), c2)
###

def cfb_encrypt(message):
    cipher = []
    cfb_iv = copy(iv)
    for message_block in message:
        cipher_block = xor(des_encrypt(cfb_iv, key), message_block)
        cfb_iv = cipher_block
        cipher.append(cipher_block)
    print_l("CFB encryption", cipher)
    return cipher

def cfb_decrypt(cipher):
    message = []
    cfb_iv = copy(iv)
    for cipher_block in cipher:
        message_block = xor(des_encrypt(cfb_iv, key), cipher_block)
        cfb_iv = cipher_block
        message.append(message_block)
    print_l("CFB decryption", message)
    return message

def cfb():
    original_cipher = cfb_encrypt(data)
    changed_cipher = shift(original_cipher, dont_shift=False)
    message = cfb_decrypt(changed_cipher)


###
# In CTR there is only a 1 bit error in the block the error occurred.
#
# For encryption:
# c0 = xor(enc(counter0, key), m0)
# c1 = xor(enc(counter1, key), m1)
# c2 = xor(enc(counter2, key), m2)
# 
# For decryption:
# m0 = xor(enc(counter0, key), c0)
# m1 = xor(enc(counter1, key), c1)
# m2 = xor(enc(counter2, key), c2)
###
def ctr_encrypt(message):
    cipher = []
    counter = copy(iv)
    for message_block in message:
        cipher_block = xor(des_encrypt(counter, key), message_block)
        counter[3] += 1
        cipher.append(cipher_block)
    print_l("CTR encryption", cipher)
    return cipher

def ctr_decrypt(cipher):
    message = []
    counter = copy(iv)
    for cipher_block in cipher:
        message_block = xor(des_encrypt(counter, key), cipher_block)
        counter[3] += 1
        message.append(message_block)
    print_l("CTR decryption", message)
    return message

def ctr():
    original_cipher = ctr_encrypt(data)
    changed_cipher = shift(original_cipher, dont_shift=False)
    message = ctr_decrypt(changed_cipher)


# Call all modes
modes = [ecb, cbc, cfb, ctr]
for mode in modes:
    mode()
    print("")
