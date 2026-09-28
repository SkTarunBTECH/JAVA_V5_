# RAIL FENCE Cipher 

def encrypt_rail_fence(plaintext, num_rails):
    # Create a list of strings for each rail
    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1      # 1 for down, -1 for up

    for char in plaintext:
        rails[rail] += char
        rail += direction

        # Change direction if we hit the top or bottom rail
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # Concatenate all rails to get the ciphertext
    ciphertext = ''.join(rails)
    return ciphertext

def decrypt_rail_fence(ciphertext, num_rails):
    # Create a list of strings for each rail
    rails = ['' for _ in range(num_rails)]
    rail_lengths = [0] * num_rails
    rail = 0
    direction = 1  # 1 for down, -1 for up

    # First, determine the length of each rail
    for char in ciphertext:
        rail_lengths[rail] += 1
        rail += direction

        # Change direction if we hit the top or bottom rail
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # Now, fill the rails with the appropriate characters from the ciphertext
    index = 0
    for i in range(num_rails):
        rails[i] = ciphertext[index:index + rail_lengths[i]]
        index += rail_lengths[i]

    # Now, read the rails in a zig-zag manner to reconstruct the plaintext
    plaintext = ''
    rail_indices = [0] * num_rails
    rail = 0
    direction = 1

    for _ in range(len(ciphertext)):
        plaintext += rails[rail][rail_indices[rail]]
        rail_indices[rail] += 1
        rail += direction

        # Change direction if we hit the top or bottom rail
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return plaintext

# Example usage
if __name__ == "__main__":
    message = "HelloWorld"
    num_rails = 2
    encrypted_message = encrypt_rail_fence(message, num_rails)
    print(f"Encrypted: {encrypted_message}")
    decrypted_message = decrypt_rail_fence(encrypted_message, num_rails)
    print(f"Decrypted: {decrypted_message}")
