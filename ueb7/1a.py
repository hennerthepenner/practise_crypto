import fractions

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount


p = 19
for a in range(1, p):
    for x in range(1, p):
        g = a ** x % p
        if g == 1:
            o = phi(x)
            print(str(a) + ": " + str(x) + ", phi: " + str(o))
            break
