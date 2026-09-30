p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter User A's private key (a): "))
b = int(input("Enter User B's private key (b): "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print(f"User A's Public Key: {A}")
print(f"User B's Public Key: {B}")

# Shared keys
k_A = pow(B, a, p)
k_B = pow(A, b, p)

print(f"Shared Key for User A: {k_A}")
print(f"Shared Key for User B: {k_B}")

if k_A == k_B:
    print("Secure Session Key Established")
else:
    print("Key Exchange Failed")
