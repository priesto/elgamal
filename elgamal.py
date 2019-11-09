# coding: utf-8

import random
import math
import collections
import string

Point = collections.namedtuple("Point", ["x", "y"])


# https://gist.github.com/bellbind/1414867#file-ecc-py
def inv(n, q):
    for i in range(q):
        if (n * i) % q == 1:
            return i
        pass
    assert False, "unreached"
    pass


def sqrt(n, q):
    assert n < q
    for i in range(1, q):
        if i * i % q == n:
            return (i, q - i)
        pass
    raise Exception("not found")

def is_valid(G):
    if G == Point(0, 0): return True
    l = (G.y ** 2) % q
    r = ((G.x ** 3) + a * G.x + b) % q
    return l == r

def pointAt(x):
    ysq = (x ** 3 + a * x + b) % q
    y, my = sqrt(ysq, q)
    return Point(x, y), Point(x, my)

def order(G):
    assert is_valid(G) and G != Point(0, 0)
    print('0: ', G)
    for i in range(1, q + 1):
        G = eccMultiply(G, i)
        print(str(i) + ': ' + str(G))
        if G == Point(0, 0):
            return i
        pass
    raise Exception("Invalid order")
pass


def eccMultiply(G, n):
    m = Point(0, 0)

    for i in range(n):
        m = eccAdd(G, m)

    return m

def eccAdd(G1, G2):
    x1 = G1.x
    x2 = G2.x

    y1 = G1.y
    y2 = G2.y

    # cas où P + O
    if G1 == Point(0, 0): return G2
    if G2 == Point(0, 0): return G1
    
    # cas où x1 = x2 et y1 = -y2
    if x1 == x2 and (y1 != y2 or y1 == 0):
        return Point(0, 0)
    
    # cas où x1 = x2 et y1 = y2
    if x1 == x2:
        l = (3 * x1 * x1 + a) * inv(2 * y1, q) % q
        pass
    
    # cas où x1 != x2
    else:
        l = (y2 - y1) * inv(x2 - x1, q) % q
        pass
    
    x = (l * l - x1 - x2) % q
    y = (l * (x1 - x) - y1) % q
    
    return Point(x, y)

    


def encrypt(G, plain, Kpub):
    rand = 7
    plain = eccMultiply(G, 5)

    print("Point sur la courbe à chiffrer :", plain)
    
    y1 = eccMultiply(G, rand)
    y2 = eccAdd(plain, eccMultiply(Kpub, rand))

    return (y1, y2)

def asciiEncrypt(m):
    rand = 7

    idx = couples.index(m) + ((rand - 1) * (Kpriv - 1))
    y1 = couples[(rand - 1) % ordre]
    y2 = couples[idx % ordre]

    return (y1, y2)
    

def decrypt(cipher, Kpriv):
    y1, y2 = cipher

    # On inverse le point y1
    y1 = eccMultiply(y1, Kpriv)
    y1 = Point(y1.x, -y1.y % q)

    return eccAdd(y2, y1)

def asciiDecrypt(y1, y2):
    idx = (couples.index(y2) - (Kpriv - 1) * couples.index(y1)) % ordre
    return couples[idx]




def generateKeypairs(G):
	Kpriv = random.randint(1, q - 1)
	Kpub = eccMultiply(G, Kpriv)

	return (Kpub, Kpriv)


def findGenerator():
    for i in range(1, q - 1):
        try:
            (g, _) = pointAt(i)
            return g
        except Exception as e:
            # no solution found
            if i == q:
                print('no solution')


def generateGenerators():
    couples = []
    for i in range(1, q - 1):
        try:
            (g, _) = pointAt(i)
            couples.append(g)
        except Exception as e:
            # no solution found
            if i == q:
                print('no solution')

    return couples

a = 4
b = 1
q = 503
m = 22


G = findGenerator()
(Kpub, Kpriv) = generateKeypairs(G)


print("Kpub, Kpriv: ", Kpub, Kpriv)


cipher = encrypt(G, m, Kpub)
print("Message chiffré :", cipher)

decoded = decrypt(cipher, Kpriv)
print("Message déchiffré :", decoded)



# Chiffrement ASCII
############################################


# Choix du meilleur générateur/ordre

ordre = 2 * q
cars = string.ascii_lowercase + "0123456789"
nb_car = len(string.ascii_lowercase + "0123456789")
message = "hello"

C = []
for x in range(1, q - 1):
    for y in range(1, q - 1):
        if(is_valid(Point(x, y))):
            C.append(Point(x, y))


points=[]
r = Point(0,0)

print("Choix du meilleur générateur/ordre...")

for i in range(len(C)):
    c = C[i]
    r = eccAdd(c, c)

    points.append(c)

    while True:
        points.append(r)
        if (r.x == c.x):
            break
        else:
            r = eccAdd(r, c)


    _ordre = len(points)
    if _ordre > nb_car and _ordre < ordre:
        ordre = _ordre
        G = points[i]

    points = []


print("Meilleur ordre : ", ordre)

print("ASCII à chiffrer : ", message)

couples = []
couples.append(G)

r = eccAdd(G, G)

while True:
    couples.append(r)
    if (r.x == G.x):
        break
    else:
        r = eccAdd(r, G)



# Chiffrement
asciiCipher = []
for m in message:
    c = couples[cars.index(m)]
    asciiCipher.append(asciiEncrypt(c))

print("ASCII chiffré : ", asciiCipher)

# Déchiffrement

asciiPlain = ""
for m in asciiCipher:
    idx = couples.index(asciiDecrypt(m[0], m[1]))
    asciiPlain += cars[idx]

print("ASCII déchiffré : ", asciiPlain)






