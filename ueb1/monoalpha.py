from collections import Counter
from static import ALPHABET
from static import PLAIN_MOST_COMMON


# Analysis of the cypher. Should return the key
def analyse(cypher):
    # Figure out the most common character in cypher text. Since this is just
    # a statistical analysis, there is no guarantee, that the most common
    # character in the cypher matches the most common character in the language
    # of the plain text. So let's assume that the correct match is somewhere
    # among the 3 most common characters. Return those and let the caller
    # decide what to do with this problem.
    most_common = Counter(cypher).most_common(3)

    # But calculate the key as distance of common characters
    possible_keys = list()
    for m in most_common:
        distance = ALPHABET.index(PLAIN_MOST_COMMON) - ALPHABET.index(m[0])
        possible_keys.append(distance)

    return possible_keys


# Decryption of monoalphabetic algothingy. Should find out the plain text
def decrypt(cypher, key):
    # Build the plain text
    plain = str()
    for c in cypher:
        # Calculate the new index for the character lookup
        plain_index = ALPHABET.index(c) + key

        # Make sure we can substitute in both directions
        if plain_index < 0:
            plain_index += len(ALPHABET)
        elif plain_index >= len(ALPHABET):
            plain_index -= len(ALPHABET)

        # Append a character to the plain text
        plain += ALPHABET[plain_index]
    return plain


# The cypher given
cypher = """Nb prkc ifnr Fnpn jdb mrnbnv Pnkjndmn: 
Dnkna mjb Pnadnbc xmna rw Qjwmblqnuunw. Knrmn brwm arbtjwc."""

# Normalize cypher to lower case characters only and stripping off everything
# that's not a character
cypher = cypher.lower().translate(None, ":. \n")

possible_keys = analyse(cypher)

# Since this is a simple exercise, we can assume, that the most common key is
# the correct one
key = possible_keys[0]

plain = decrypt(cypher, key)
print(plain)

