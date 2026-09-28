# Function to compute gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute Euler's Totient φ(n)
def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:   # Count numbers coprime with n
            count += 1
    return count

# Read integers a and n
a = int(input("Enter integer a: "))
n = int(input("Enter integer n: "))

phi_n = euler_totient(n)
print("φ(n) =", phi_n)

# Check coprime
if gcd(a, n) != 1:
    print("a and n are not coprime.")
else:
    # Compute a^φ(n) mod n
    result = pow(a, phi_n, n)
    print("Result =", result)
