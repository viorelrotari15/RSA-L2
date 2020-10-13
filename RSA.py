

import random

'''
Calculeaza totientul numarului prim

Totient - Indicatorul lui Euler sau funcția lui Euler se notează cu φ și φ reprezintă numărul de numere mai mici sau egale cu n și prime cu acesta
'''


def totient(number):
    if (prime(number)):
        return number - 1
    else:
        return False


'''
Verifica daca numarul este prim 
'''


# Metoda de calculare a numerelor prime
def prime(n):  # verifica daca numarul este prim
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True


'''
Generează un număr aleatoriu E, care îndeplinește condițiile
'''


def generate_E(num):
    def mdc(n1, n2):
        rest = 1
        while (n2 != 0):
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2, num)
        if (mdc(num, e) == 1):
            return e


'''
Generează un număr prim aleator
'''


def generate_prime():  # genereaza numerele prime - p e q
    while True:  # 2**2048 este metoda RSA standart key
        x = random.randrange(1, 100)  # defineste gama numerelor prime
        if (prime(x) == True):
            return x


'''
Funcție modulară între două numere
'''


def mod(a, b):
    if (a < b):
        return a
    else:
        c = a % b
        return c


'''
Criptează un text
'''


def cipher(words, e, n):  # obține cuvintele și calculează cifrul
    tam = len(words)
    i = 0
    lista = []
    while (i < tam):
        letter = words[i]
        k = ord(letter)
        k = k ** e
        d = mod(k, n)
        lista.append(d)
        i += 1
    return lista


'''
Decriptează textul criptat
'''


def descifra(cifra, n, d):
    lista = []
    i = 0
    tamanho = len(cifra)
    # text=cifra ^ d mod n
    while i < tamanho:
        result = cifra[i] ** d
        texto = mod(result, n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista


'''
Calculează cheia privată
'''


def calculate_private_key(toti, e):
    d = 0
    while (mod(d * e, toti) != 1):
        d += 1
    return d


## MAIN
if __name__ == '__main__':
    text = input("Insert message: ")
    p = generate_prime()  # genereaza random P
    q = generate_prime()  # genereaza random Q
    n = p * q  # calculeaza N
    y = totient(p)  # calculeaza  totient lui P
    x = totient(q)  # calculeaza totient lui Q
    totient_de_N = x * y  # calculeaza  totient lui N
    e = generate_E(totient_de_N)  # genereaza E
    public_key = (n, e)

    print('Your public key:', public_key)
    text_cipher = cipher(text, e, n)
    print('Your encrypted message:', text_cipher)
    d = calculate_private_key(totient_de_N, e)
    print('Your private key is:', d)
    original_text = descifra(text_cipher, n, d)
    print('your original message:', original_text)