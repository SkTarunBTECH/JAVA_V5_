# Monoalphabetic Cipher

def normalize_key(key):
    # Remove duplicates and non-alphabetic characters, and create a full 26-letter mapping
    letters = [c.lower() for c in key if c.isalpha()]
    seen = set()
    result = []
    for c in letters:
        if c not in seen:
            seen.add(c)
            result.append(c)
    for i in range(26):
        ch = chr(ord('a') + i)
        if ch not in seen:
            result.append(ch)
    return ''.join(result)

def encrypt_monoalphabetic(plaintext, key):
    ciphertext = ""
    # Ensure key is a full 26-letter mapping (generate from keyword if needed)
    key = normalize_key(key)
    key_map = {chr(i + ord('a')): key[i] for i in range(26)}
    
    for char in plaintext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            char_lower = char.lower()
            # Substitute the character using the key map
            substituted_char = key_map[char_lower]
            # Convert back to uppercase if necessary
            if is_upper:
                substituted_char = substituted_char.upper()
            ciphertext += substituted_char
        else:
            # Non-alphabetic characters are not changed
            ciphertext += char
            
    return ciphertext

def decrypt_monoalphabetic(ciphertext, key):
    plaintext = ""
    key = normalize_key(key)
    reverse_key_map = {key[i]: chr(i + ord('a')) for i in range(26)}
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            char_lower = char.lower()
            # Substitute the character using the reverse key map
            substituted_char = reverse_key_map[char_lower]
            # Convert back to uppercase if necessary
            if is_upper:
                substituted_char = substituted_char.upper()
            plaintext += substituted_char
        else:
            # Non-alphabetic characters are not changed
            plaintext += char
            
    return plaintext

# Example usage
if __name__ == "__main__":
    message = "HelloWorld!"
    key = "cases"         # Example keyword — can be short; will be expanded

    encrypted_message = encrypt_monoalphabetic(message, key)
    print(f"Encrypted: {encrypted_message}")
    
    decrypted_message = decrypt_monoalphabetic(encrypted_message, key)
    print(f"Decrypted: {decrypted_message}")

