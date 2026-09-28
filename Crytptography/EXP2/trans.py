import string
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def preprocess_text(text: str) -> str:
    """Converts to uppercase and removes non-alphabetic characters."""
    return re.sub(r'[^A-Z]', '', text.upper())

def rail_fence_encrypt(plaintext: str, num_rails: int) -> str:
    """Encrypts plaintext using the Rail Fence transposition cipher."""
    if num_rails <= 1 or len(plaintext) <= num_rails:
        return plaintext
        
    rails = [''] * num_rails
    current_rail = 0
    direction = 1
    
    for char in plaintext:
        rails[current_rail] += char
        current_rail += direction
        
        # Reverse direction at the top or bottom rail
        if current_rail == 0 or current_rail == num_rails - 1:
            direction *= -1
            
    return ''.join(rails)

def get_frequency_distribution(text: str) -> dict[str, int]:
    """Calculates the absolute frequency of each letter A-Z."""
    counts = Counter(text)
    return {char: counts.get(char, 0) for char in string.ascii_uppercase}

# Execution based on provided experimental data
if __name__ == "__main__":
    raw_plaintext = "WE ARE DISCOVERED FLEE AT ONCE"
    rails_count = 3
    
    # Preprocessing & Encryption
    plaintext = preprocess_text(raw_plaintext)
    ciphertext = rail_fence_encrypt(plaintext, rails_count)
    
    print(f"Plaintext: {raw_plaintext}")
    print(f"Rail Fence Ciphertext: {ciphertext}\n")
    
    # Frequency Analysis
    pt_freq = get_frequency_distribution(plaintext)
    ct_freq = get_frequency_distribution(ciphertext)
    
    # Comparison Table Output
    print(f"{'Letter':<10} | {'Plaintext Count':<16} | {'Ciphertext Count'}")
    print("-" * 48)
    for char in string.ascii_uppercase:
        print(f"{char:<10} | {pt_freq[char]:<16} | {ct_freq[char]}")
        
    # Visualization: Grouped Bar Chart
    labels = list(string.ascii_uppercase)
    pt_values = list(pt_freq.values())
    ct_values = list(ct_freq.values())
    
    x = np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x - width/2, pt_values, width, label='Plaintext', color='blue', alpha=0.7)
    ax.bar(x + width/2, ct_values, width, label='Rail Fence Ciphertext', color='orange', alpha=0.7)
    
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Plaintext vs Rail Fence Ciphertext Frequency')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    plt.tight_layout()
    plt.show()
    