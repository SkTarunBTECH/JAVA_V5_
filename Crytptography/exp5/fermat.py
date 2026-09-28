# Fermat's Little Theorem
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Read integer a and prime number p
a = int(input("Enter integer a: "))
p = int(input("Enter prime number p: "))

# Check if a and p are coprime
if gcd(a, p) != 1:
    print("a and p are not coprime.")
else:
    # Compute a^(p-1) mod p
    result = pow(a, p - 1, p)
    print("Result =", result)
