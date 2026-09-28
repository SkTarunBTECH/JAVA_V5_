import random
import time

# Read integer n
n = int(input("Enter an integer: "))

# Record start time
start = time.time()

# Check primality using Fermat's test
if n <= 1:
    print("Composite")
elif n == 2 or n == 3:
    print("Prime")
elif n % 2 == 0:
    print("Composite")
else:
    # Choose random a in [2, n-2]
    a = random.randint(2, n - 2)
    # Compute a^(n-1) mod n
    result = pow(a, n - 1, n)
    if result != 1:
        print("Composite")
    else:
        print("Probably Prime")

# Record end time
end = time.time()

# Display execution time
print("Execution time =", end - start, "seconds")
