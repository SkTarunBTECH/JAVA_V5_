# CAESAR Cipher encryption and decryption

def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
    # Determine if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
    # Shift the character and wrap around the alphabet
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += shifted_char
        else:
    # Non-alphabetic characters are not changed
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
    # Determine if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
    # Shift the character back and wrap around the alphabet
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += shifted_char
        else:
    # Non-alphabetic characters are not changed
            plaintext += char     
    return plaintext

# Example usage
if __name__ == "__main__":
    message = "Hello, World!"
    shift_value = 3
    
    encrypted_message = encrypt_caesar(message, shift_value)
    print(f"Encrypted: {encrypted_message}")
    
    decrypted_message = decrypt_caesar(encrypted_message, shift_value)
    print(f"Decrypted: {decrypted_message}")