from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate 2048-bit RSA key pair
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

# Display keys
print("Public Key:\n", public_key.export_key().decode())
print("Private Key:\n", private_key.export_key().decode())

# Read plaintext message
message = input("Enter message: ")
plaintext = message.encode()

# Encrypt with public key
cipher_pub = PKCS1_OAEP.new(public_key)
ciphertext = cipher_pub.encrypt(plaintext)
print("Ciphertext (hex):", ciphertext.hex())

# Decrypt with private key
cipher_priv = PKCS1_OAEP.new(private_key)
decrypted = cipher_priv.decrypt(ciphertext)
print("Decrypted message:", decrypted.decode())
