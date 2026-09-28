# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m

# Chinese Remainder Theorem
def chinese_remainder(a_list, m_list):
    M = 1
    for m in m_list:       # Product of all moduli
        M *= m

    x = 0
    for ai, mi in zip(a_list, m_list):
        Mi = M // mi       # Partial product
        inv = mod_inverse(Mi, mi)  # Modular inverse
        x += ai * Mi * inv

    return x % M           # Final solution

# Read number of congruences
n = int(input("Enter number of congruenceEquations: "))

a_list = []
m_list = []

for i in range(n):
    ai = int(input(f"Enter remainder a{i+1}: "))
    mi = int(input(f"Enter modulus m{i+1}: "))
    a_list.append(ai)
    m_list.append(mi)

solution = chinese_remainder(a_list, m_list)
print("Solution x =", solution)
