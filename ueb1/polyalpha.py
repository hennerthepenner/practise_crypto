from collections import Counter
from fractions import gcd
from itertools import product
import re
import monoalpha
from static import ALPHABET
from static import PLAIN_MOST_COMMON


# Analysis of the cypher. Should return the key
def analyse(cypher):
    # Figure out repeated groups of more than 2 characters. To make it easy,
    # let's say we use exactly 3 characters
    groups = [cypher[i:i + 3] for i in range(0, len(cypher) - 2)]

    # Assume that our cypher is very long and we can find many groups. Let's
    # use the 3 most common groups
    # Example: gov (12x), ovg (11x), tov (11x)
    common_groups = Counter(groups).most_common(3)

    # Make a list of distances between the occurences of the common groups
    distances = list()
    for [group, occurences] in common_groups:
        last_match = None
        for match in re.finditer(group, cypher):
            if last_match:
                distance = match.start() - last_match.start()
                distances.append(distance)
            last_match = match

    # Knowing the distances, it's easy to calculate the gcd of the distances.
    # This can be extremely tricky, if there are coinciding groups, which isn't
    # handled at all
    # Example: 3
    key_length = reduce(gcd, distances)

    # Reorder the cypher in columns according to the key length
    columns = [""] * key_length
    column_counter = 0
    for c in cypher:
        columns[column_counter] += c
        column_counter += 1
        if column_counter == key_length:
            column_counter = 0

    # Use the monoalphabetic analysis tool to calculate the key for each
    # column
    possible_keys = [monoalpha.analyse(col) for col in columns]
    return list(product(*possible_keys))


# Decryption of polyalphabetic algothingy. Should find out the plain text
def decrypt(cypher, key):
    plain = str()
    column_counter = 0
    for c in cypher:
        # Decrypt one character using the key in the correct column
        plain += monoalpha.decrypt_character(c, key[column_counter])

        column_counter += 1
        if column_counter == len(key):
            column_counter = 0

    return plain

# The cypher given
cypher = """Cjgt K hopf sa eufg op vupu uh vxqwhng,
Ltkkpfy cpj eqrnggiwku euog zq ok,
Urkcmopi cqtju ql ykyfqs:
"Ytovg op E."
Gu vng fkcfrkpk hcyv cvrtucengu,
Gpf hwiy ctk cnr vjgv K icp ygg,
Yqokyjktg, yqokqpk yjourktu:
"Ctkzg kt E."
Yxkvk kp I, Ytovg op E,
Ctkzg kt E, qn, Ytovg op E.
RQIUu fkcf gpf hwtogf,
Ctkzg kt E.
K augj vq ctkzg c rqv uh HUTVXCP,
Lqt yekkpek kv cqtqgf lnccngyune.
Vte wuopi ov hut ixcrnkey!
Ytovg op E.
Oh auwxk lwyv uvgpz pggtne 30 jqatu
Jgdaiiopi yqok cuygohna,
Yqqt aqa ykrn dk ingf vu
Ytovg op E.
Ctkzg kt E, Yxkvk kp I,
Ytovg op E, egcn, Ytovg op E.
Dnkna mjb Pnadnbc
Upne yksru aug HCUOE.
Yxkvk kp I.
Ytovg op E, Ctkzg kt E
Yxkvk kp I, qj, Ctkzg kt E.
Rguegn yupv wwkzg eav kz.
Ytovg op E.
Ctkzg kt E, Yxkvk kp I,
Ytovg op E, egcn, Ytovg op E.
Jqpz gxkp okpvoqp IQDUN.
Yxkvk kp I.
(cpj yjgv chqwz E++ ?)
- Dxkct Ocxujgnn, Ctkzg kt E"""

# Normalize cypher to lower case characters only and stripping off everything
# that's not a character
cypher = cypher.lower().translate(None, " ,:\".\n!30(+?)-")

possible_keys = analyse(cypher)

# Print all possible 3^3 solutions
for key in possible_keys:
    plain = decrypt(cypher, key)
    print("Possible solution using key " + str(key) + ":")
    print(plain + "\n")

# Hardcode the correct key
key = possible_keys[13]
print("The solution with key " + str(key) + ":")
print(decrypt(cypher, key))
