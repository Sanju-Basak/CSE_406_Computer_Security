import random
import time

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
        
def generate_safe_prime_number(n):
    # n is the number of bits of the safe prime number
    # return a safe prime number p
    while True:
        q = generate_prime_number(n - 1)
        p = 2 * q + 1
        if miller_rabin_test(p, 100):
            return p
        
def generate_generator(p):
    # p is a prime number
    # return a generator g of Zp*
    while True:
        g = random.randint(2, p - 1)
        if modular_exponent(g, (int)((p - 1) / 2), p) != 1 and modular_exponent(g, 2, p) != 1:
            return g
        
def calculate_public_key(g, p, private_key):
    return modular_exponent(g, private_key, p)

def calculate_shared_key(public_key, private_key, p):
    return modular_exponent(public_key, private_key, p)


# for k in [128, 192, 256]:
#     sum_time_primes= 0
#     sum_time_generator= 0
#     sum_time_a= 0
#     sum_time_A= 0
#     sum_time_shared= 0

#     for i in range(5):
#         start_time_primes= time.time()
#         p= generate_safe_prime_number(k)
#         end_time_primes= time.time()
#         sum_time_primes+= end_time_primes - start_time_primes
#         start_time_generator= time.time()
#         g= generate_generator(p)
#         end_time_generator= time.time()
#         sum_time_generator+= end_time_generator - start_time_generator
#         start_time_a= time.time()
#         a= generate_safe_prime_number(k/2)
#         end_time_a= time.time()
#         sum_time_a+= end_time_a - start_time_a
#         b= generate_safe_prime_number(k/2)
#         start_time_A= time.time()
#         A= calculate_public_key(g, p, a)
#         end_time_A= time.time()
#         sum_time_A+= end_time_A - start_time_A
#         B= calculate_public_key(g, p, b)
#         start_time_shared= time.time()
#         shared_key1= calculate_shared_key(A, b, p)
#         end_time_shared= time.time()
#         shared_key2= calculate_shared_key(B, a, p)
#         sum_time_shared+= end_time_shared - start_time_shared
#         print("shared_key1= ", shared_key1)
#         print("shared_key2= ", shared_key2)
#         print("")
#     print("k= ", k)
#     print("Average time of generating prime numbers: ", sum_time_primes/5, " seconds")
#     print("Average time of generating generators: ", sum_time_generator/5, " seconds")
#     print("Average time of generating private keys: ", sum_time_a/5, " seconds")
#     print("Average time of generating public keys: ", sum_time_A/5, " seconds")
#     print("Average time of generating shared keys: ", sum_time_shared/5, " seconds")
#     print("")
#     sum_time_primes= 0
#     sum_time_generator= 0
#     sum_time_a= 0
#     sum_time_A= 0
#     sum_time_shared= 0

# i= 0
# while i in range(5):
#     k= 128
#     time_primes= time.time()
#     p= generate_safe_prime_number(k)
#     time_primes= time.time() - time_primes
#     g= generate_generator(p)
#     a= generate_safe_prime_number(k/2)
#     b= generate_safe_prime_number(k/2)

#     A= calculate_public_key(g, p, a)
#     B= calculate_public_key(g, p, b)

#     shared_key1= calculate_shared_key(A, b, p)
#     shared_key2= calculate_shared_key(B, a, p)

#     print("time= ", time_primes, " s")

#     print(shared_key1)
#     print(shared_key2)
#     i+= 1





