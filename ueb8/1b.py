# -*- coding: UTF-8 -*-

from elliptic import add
from elliptic import double
from elliptic import multiply


# Gegeben
P = [3,3]
a = 3
b = 19
m = 23  # modulo (aka p)

print("1.b.i) 2P")
double(P, a, m)
print("")

print("1.b.ii) 3P = 2P + P")
multiply(P, 3, a, m)
print("")

print("1.b.iii) für Schlaumeier: 6P = 2 * 3P")
P3 = multiply(P, 3, a, m)
double(P3, a, m)
print("")

print("1.b.iii) für Mathematiker: 6P = 2P + P + P + P + P")
multiply(P, 6, a, m)
print("")

print("1.b.iv) P+Q=R mit Q=[4,7]")
Q = [4,7]
add(P, Q, m)
print("")

print("1.b.v) P+Q=R mit Q=[3,20]")
Q = [3,20]
add(P, Q, m)
print("")
