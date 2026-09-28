# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:              # Base case
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)  # Recursive call
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Read two integers
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

gcd, x, y = extended_gcd(a, b)
print("GCD =", gcd)
print("x =", x)
print("y =", y)

# Modular inverse if GCD = 1

if gcd == 1:
    mod_inverse = x % b
    print("Modular Inverse =", mod_inverse)
