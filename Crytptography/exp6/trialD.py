import time
import math

n = int(input("Enter an integer: "))        # Read integer n

start = time.time()     # Record start time

# Check primality
if n <= 1:
    print("Invalid")
    # return False
else:
    prime = True
    for i in range(2, int(math.sqrt(n)) + 1):  # Check divisibility up to √n
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Composite")

end = time.time()       # Record end time

# Display execution time
print("Execution time =", end - start, "seconds")
