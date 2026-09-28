import random
import time

                        # Miller–Rabin Primality Test
                        
def is_prime(n, k=5):   # k = number of iterations
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d with d odd
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k iterations
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False   # Composite
    return True            # Probably Prime

n = int(input("Enter an integer: "))        # Read integer n

start = time.time()

# Run Miller–Rabin test
if is_prime(n):
    print("Probably Prime")
else:
    print("Composite")


end = time.time()
print("Execution time =", end - start, "seconds")
