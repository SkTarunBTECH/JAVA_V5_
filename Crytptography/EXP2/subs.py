#  Perform cryptanalysis of substitution ciphers using frequency analysis and statistical methods. 
from collections import Counter
import matplotlib.pyplot as plt
import string

def preprocess(text):
    """Convert to uppercase and keep only A-Z letters."""
    return ''.join([c for c in text.upper() if c.isalpha()])

# Caesar Cipher + Frequency Analysis (minimal, lab-friendly changes)
def caesar_cipher_analysis(message, shift):
    # Encrypt
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char

    # Decrypt
    decrypted = ""
    for char in encrypted:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char

    # Preprocess for frequency analysis (uppercase, letters only)
    processed = preprocess(encrypted)
    counter = Counter(processed)
    total = sum(counter.values())
    freq_percent = {letter: (counter[letter] / total * 100) if total > 0 else 0 for letter in string.ascii_uppercase}

    # Print Results (preserve original outputs)
    print(f"Plaintext: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}\n")

    # Frequency Analysis A-Z
    print("Frequency Analysis (A-Z):")
    for letter in string.ascii_uppercase:
        print(f"{letter}: {counter[letter]} ({freq_percent[letter]:.2f}%)")

    # Display six most frequent characters (required by lab)
    print("\nTop 6 most frequent characters in ciphertext:")
    for letter, cnt in counter.most_common(6):
        pct = (cnt / total * 100) if total > 0 else 0
        print(f"{letter}: {cnt} ({pct:.2f}%)")

    # Standard English frequencies for common letters (lab requirement)
    english_freq = {'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7}
    print("\nComparison with standard English frequencies (for top letters):")
    for letter, cnt in counter.most_common(6):
        cipher_pct = freq_percent[letter]
        eng_pct = english_freq.get(letter, 0.0)
        print(f"{letter}: ciphertext {cipher_pct:.2f}%  |  English (if common) {eng_pct:.2f}%")

    # Plot
    plt.bar(list(string.ascii_uppercase), [freq_percent[l] for l in string.ascii_uppercase])
    plt.title("Caesar Cipher Frequency Distribution")
    plt.xlabel("Letters")
    plt.ylabel("Frequency (%)")
    plt.show()

# Example usage with user input (easy to run in lab)
if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    try:
        shift_val = int(input("Enter Caesar shift (0-25): "))
    except ValueError:
        print("Invalid shift; using 3 by default.")
        shift_val = 3
    caesar_cipher_analysis(plaintext, shift_val)

#-------------------------------------------






























from collections import Counter
import matplotlib.pyplot as plt
import string

# Caesar Cipher + Frequency Analysis
def caesar_cipher_analysis(message, shift):
    # Encrypt
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char

    # Decrypt
    decrypted = ""
    for char in encrypted:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char

    # Frequency Analysis
    processed = ''.join([c.upper() for c in encrypted if c.isalpha()])
    counter = Counter(processed)
    total = sum(counter.values())
    freq_percent = {letter: (counter[letter] / total * 100) if total > 0 else 0 for letter in string.ascii_uppercase}

    # Print Results
    print(f"Plaintext: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}\n")
    print("Frequency Analysis:")
    for letter in string.ascii_uppercase:
        print(f"{letter}: {counter[letter]} ({freq_percent[letter]:.2f}%)")

    # Plot
    plt.bar(list(string.ascii_uppercase), [freq_percent[l] for l in string.ascii_uppercase])
    plt.title("Caesar Cipher Frequency Distribution")
    plt.xlabel("Letters")
    plt.ylabel("Frequency (%)")
    plt.show()

# Example usage
if __name__ == "__main__":
    caesar_cipher_analysis("Hello, World!", 3)
