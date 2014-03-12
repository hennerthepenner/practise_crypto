from collections import Counter
from static import ALPHABET
from static import PLAIN_MOST_COMMON


# Analysis of the cypher. Should return the key
def analyse(cypher):
    # Figure out the most common character in cypher text
    [cypher_most_common, occurences] = Counter(cypher).most_common(1)[0]

    # Then it's easy to calculate the key
    key = ALPHABET.index(PLAIN_MOST_COMMON) - ALPHABET.index(cypher_most_common)
    return key


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
        elif plain_index > len(ALPHABET):
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

key = analyse(cypher)
plain = decrypt(cypher, key)
print(plain)

