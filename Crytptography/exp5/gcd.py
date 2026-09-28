# Euclid's Algorithm to find GCD
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

while b != 0:          # Repeat until remainder becomes 0
    remainder = a % b  # Compute remainder
    a = b              # Update a
    b = remainder      # Update b

print("GCD =", a)      # Display the result
