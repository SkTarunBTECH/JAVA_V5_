# Vigenere cipher

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            char_lower = char.lower()
            # Get the corresponding key character
            key_char = key[key_index % key_length].lower()
            # Calculate the shift
            shift = ord(key_char) - ord('a')
            # Encrypt the character
            encrypted_char = chr((ord(char_lower) - ord('a') + shift) % 26 + ord('a'))
            # Convert back to uppercase if necessary
            if is_upper:
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters are not changed
            ciphertext += char
            
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            char_lower = char.lower()
            # Get thA corresponding key character
            key_char = key[key_index % key_length].lower()
            # Calculate the shift
            shift = ord(key_char) - ord('a')
            # Decrypt the character
            decrypted_char = chr((ord(char_lower) - ord('a') - shift) % 26 + ord('a'))
            # Convert back to uppercase if necessary
            if is_upper:
                decrypted_char = decrypted_char.upper()
            plaintext += decrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters are not changed
            plaintext += char
            
    return plaintext

# Example usage
if __name__ == "__main__":
    message = "HelloWorld!"
    key = "keyword"

    encrypted_message = vigenere_encrypt(message, key)
    print(f"Encrypted: {encrypted_message}")
    decrypted_message = vigenere_decrypt(encrypted_message, key)
    print(f"Decrypted: {decrypted_message}")
