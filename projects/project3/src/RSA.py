import random
import math
from typing import Tuple, Optional

def miller_rabin_test(n: int, k: int = 5) -> bool:
    
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Perform k rounds of testing
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

def generate_prime(bits: int) -> int:
    
    while True:
        # Generate random odd number with specified bits
        candidate = random.getrandbits(bits)

        # Ensure it's odd and has the right bit length
        candidate |= (1 << bits - 1) | 1
        
        if miller_rabin_test(candidate):
            return candidate

def euclidean_algorithm(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a: int, b: int) -> Tuple[int, int, int]:
    
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

def modular_inverse(e: int, phi_n: int) -> Optional[int]:
    
    gcd, x, _ = extended_euclidean_algorithm(e, phi_n)
    
    if gcd != 1:
        return None  # Modular inverse doesn't exist
    
    return (x % phi_n + phi_n) % phi_n

def powmod_sm(base: int, exponent: int, modulus: int) -> int:
    
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    
    return result

def rsa_key_generation(s: int = 512) -> Tuple[Tuple[int, int], int]:
    
    print(f"Generating RSA keys with {s}-bit primes:")
    
    #Chooses two distinct primes p and q
    print("Generating prime p:")
    p = generate_prime(s)
    print("Generating prime q:")
    q = generate_prime(s)
    
    # Ensures p != q
    while p == q:
        q = generate_prime(s)
    
    print(f"p = {p}")
    print(f"q = {q}")
    
    #Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    print(f"n = p * q = {n}")
    print(f"phi(n) = (p-1) * (q-1) = {phi_n}")
    
    #Choose e such that gcd(e, phi(n)) = 1
    print("Choosing e:")
    while True:
        e = random.randrange(2, phi_n)
        if euclidean_algorithm(e, phi_n) == 1:
            break
    
    print(f"e = {e}")
    
    #Calculate d = e^(-1) mod phi(n)
    print("Calculating d:")
    d = modular_inverse(e, phi_n)
    
    # Checks if d is at least 0.3 * s bits
    min_d_bits = int(0.3 * s)
    while d is None or d.bit_length() < min_d_bits:
        e = random.randrange(2, phi_n)
        if euclidean_algorithm(e, phi_n) == 1:
            d = modular_inverse(e, phi_n)
    
    print(f"d = {d}")
    print(f"d has {d.bit_length()} bits (minimum required: {min_d_bits})")
    
    #Output keys
    public_key = (n, e)
    private_key = d
    
    return public_key, private_key

def rsa_encryption(public_key: Tuple[int, int], plaintext: int) -> int:
    
    n, e = public_key
    ciphertext = powmod_sm(plaintext, e, n)
    return ciphertext

def rsa_decryption(private_key: int, ciphertext: int, n: int) -> int:
    
    plaintext = powmod_sm(ciphertext, private_key, n)
    return plaintext

def main():
    
    print("RSA CRYPTOSYSTEM IMPLEMENTATION")
    
    
    #RSA Key Generation
    print("\n1. RSA KEY GENERATION")
    s = 512  # bit length
    public_key, private_key = rsa_key_generation(s)
    n, e = public_key
    d = private_key
    
    print(f"\nPublic Key (n, e):")
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"\nPrivate Key (d):")
    print(f"d = {d}")
    
    #RSA Encryption
    print(f"\n2. RSA ENCRYPTION")
    
    
    # Generate random plaintext in range [1, n-1]
    max_plaintext = n - 1
    plaintext = random.randrange(1, min(max_plaintext, 2**100))
    


    print(f"Original plaintext: {plaintext}")
    
    ciphertext = rsa_encryption(public_key, plaintext)
    print(f"Encrypted ciphertext: {ciphertext}")
    
    #RSA Decryption
    print(f"\n3. RSA DECRYPTION")
    
    
    decrypted_plaintext = rsa_decryption(private_key, ciphertext, n)
    print(f"Decrypted plaintext: {decrypted_plaintext}")
    
    #Verification
    print(f"\n4. VERIFICATION")
    
    print(f"Original plaintext:  {plaintext}")
    print(f"Decrypted plaintext: {decrypted_plaintext}")
    print(f"Match: {plaintext == decrypted_plaintext}")
    
    #Key Verification    
    print(f"\n5. KEY VERIFICATION")
    
    # Simple test message :D
    test_message = plaintext
    if test_message < n:
        encrypted_test = rsa_encryption(public_key, test_message)
        decrypted_test = rsa_decryption(private_key, encrypted_test, n)
        print(f"Test message: {test_message}")
        print(f"After encrypt->decrypt: {decrypted_test}")
        print(f"Key pair works correctly: {test_message == decrypted_test}")

if __name__ == "__main__":
    random.seed(101020120)
    main()