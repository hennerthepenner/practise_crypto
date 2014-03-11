from collections import Counter

# The cypher given
cypher = """Nb prkc ifnr Fnpn jdb mrnbnv Pnkjndmn: 
Dnkna mjb Pnadnbc xmna rw Qjwmblqnuunw. Knrmn brwm arbtjwc."""

# Normalize cypher to lower case characters only and stripping off everything
# that's not a character
cypher = cypher.lower().translate(None, ":. \n")

# Define the basic plain text data (should be given)
alphabet = "abcdefghijklmnopqrstuvwxyz"
plain_most_common = "e"  # German: 14%, English: 12%

# Figure out the most common character in cypher text
[cypher_most_common, occurences] = Counter(cypher).most_common(1)[0]

# Then it's easy to calculate the key
key = alphabet.index(plain_most_common) - alphabet.index(cypher_most_common)

# Build the plain text
plain = str()
for c in cypher:
    plain_index = alphabet.index(c) + key
    # Make sure we can substitute in both directions
    if plain_index < 0:
        plain_index += len(alphabet)
    plain += alphabet[plain_index]

print(plain)
