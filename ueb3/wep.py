from operator import xor


# Use key 0x0227
key = [0x0, 0x2, 0x2, 0x7]

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
