def mult_inv(P, m):
    i = 1
    while (P * i) % m != 1:
        i += 1
    return i

def makeX(S, P, Q, m):
    x = (S ** 2 - P[0] - Q[0]) % m
    while x < 0:
        x += m
    return x

def makeY(S, P, R, m):
    y = (S * (P[0] - R[0]) - P[1]) % m
    while y < 0:
        y += m
    return y

def double(P, a, m):
    S = ((3 * (P[0]**2) + a) % m) * mult_inv((2 * P[1]) % m, m) % m
    print("S: " + str(S))
    R = []
    R.append(makeX(S, P, P, m))
    R.append(makeY(S, P, R, m))
    print("R: " + str(R))
    return R

def add(P, Q, m):
    if P[0] == Q[0]:
        print("R = O")
        return [0,0]

    S = (Q[1] - P[1] % m) * mult_inv((Q[0] - P[0]) % m, m) % m
    print("S: " + str(S))
    R = []
    R.append(makeX(S, P, Q, m))
    R.append(makeY(S, P, R, m))
    print("R: " + str(R))
    return R

def multiply(P, times, a, m):
    R = double(P, a, m)
    if times <= 0:
        raise Error("times must be greater than 0")
    if times == 1:
        return P
    elif times == 2:
        return R
    else:
        i = 2
        while times - i > 0:
            R = add(P, R, m)
            i += 1
        return R
