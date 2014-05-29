from operator import xor


# Use key 0xAFFE
key = [0xA, 0xF, 0xF, 0xE]

# KSA algorithm
print("KSA")

# Fill s with increasing number
s = [i for i in range(0, 16)]

j = 0
for i in range(0, 16):
    # Build j
    j = (key[i % len(key)] + s[i] + j) % 16
    # Swap values in s
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp

    print("i: %#x, j: %#x, s: %s" % (i, j, "".join(["%#x, " % b for b in s])))

# PRGA algorithm
print("PRGA")

msg = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]
cipher = list()

i = 0
j = 0
for m in msg:
    # Get new indeces
    i = (i + 1) % 16
    j = (j + s[i]) % 16

    # Swap values
    tmp = s[i]
    s[i] = s[j]
    s[j] = tmp

    # Build the output byte
    x = s[(s[i] + s[j]) % 16]

    # XOR the message with the cipher stream
    c = xor(x, m)
    cipher.append(c)

    print("i: %#x, j: %#x, x: %#x, c: %#x" % (i, j, x, c))
    print("s: %s" % "".join(["%#x, " % b for b in s]))
    print("")

print("Cipher: %s" % "".join(["%#x, " % b for b in cipher]))
