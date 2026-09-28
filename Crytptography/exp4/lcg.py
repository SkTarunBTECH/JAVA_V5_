import numpy as np
import matplotlib.pyplot as plt

def lcg(seed, a, c, m, n): 
    x = seed
    numbers = []
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)
    return np.array(numbers)

# Input parameters
seed = int(input("Enter seed value X0: "))
a = int(input("Enter multiplier a: "))
c = int(input("Enter increment c: "))
m = int(input("Enter modulus m: "))
n = int(input("Enter number of pseudorandom numbers n: "))

# Generate numbers
nums = lcg(seed, a, c, m, n)

# Mean, variance
mean_val = np.mean(nums)
var_val = np.var(nums)

# Frequency count
unique, freq = np.unique(nums, return_counts=True)

# Display results
print("\nGenerated Numbers:\n", nums)
print("\nMean =", mean_val)
print("Variance =", var_val)

# Plot frequency distribution
plt.bar(unique, freq)
plt.title("LCG Frequency Distribution")
plt.xlabel("Generated Values")
plt.ylabel("Frequency")
plt.show()
