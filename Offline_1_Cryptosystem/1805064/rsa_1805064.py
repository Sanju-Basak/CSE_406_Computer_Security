import random

def modular_exponent(base, exponent, modulus):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    return result

def miller_rabin_test(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write (n - 1) as 2^r * d, where d is an odd number
    r=0
    d=n-1

    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform the Miller-Rabin test k times
    for i in range(k):
        a = random.randint(2, n - 2)
        x = modular_exponent(a, d, n)  # Compute a^d % n

        if x == 1 or x == n - 1:
            continue

        for j in range(r - 1):
            x = modular_exponent(x, 2, n)  # Compute x^2 % n

            if x == n - 1:
                break
        else:
            return False  # n is composite

    return True  # n is probably prime

def generate_prime_number(n):
    # n is the number of bits of the prime number
    # return a prime number p
    while True:
        p = random.randint(pow(2, n - 1), pow(2, n) - 1)
        if miller_rabin_test(p, 100):
            return p

def modInverse(A, M):
    m0 = M
    y = 0
    x = 1
 
    if (M == 1):
        return 0
 
    while (A > 1):
 
        # q is quotient
        q = A // M
 
        t = M
 
        # m is remainder now, process
        # same as Euclid's algo
        M = A % M
        A = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x


def gcd(a, b):
    # return gcd(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)

def rsa_algorithm(p, q):
    # p and q are prime numbers
    # return n, e, d
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    d = modInverse(e, phi)

    return n, e, d

def encrypt(public_key, message):
    e, n = public_key
    encrypted_msg = [modular_exponent(ord(char), e, n) for char in message]
    return encrypted_msg

def decrypt(private_key, encrypted_msg):
    d, n = private_key
    for i in range(len(encrypted_msg)):
        encrypted_msg[i]= chr(modular_exponent(encrypted_msg[i], d, n))
    return ''.join(encrypted_msg)

p= generate_prime_number(128)
while True:
    q= generate_prime_number(128)
    if q!= p:
        break

n, e, d= rsa_algorithm(p, q)

M= "Hello World! You are awesome!"

print("\n\nBefore encryption, Message =", M)
C= encrypt((e, n), M)
print("\n\nAfter encryption, Ciphertext =", C)
M= decrypt((d, n), C)
print("\n\nAfter decryption, Message =", M)
