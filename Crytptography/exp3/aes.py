# !pip install pycryptodome  AES Algorithm

import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def run_aes_experiment() -> None:    
    # Steps 1 & 2: Read plaintext and key
    plaintext = input("Enter the plaintext: ")
    key_input = input("Enter a 16-character key: ")
    
    # Step 3: Check key length
    if len(key_input) != 16:
        print("Error: Key must be exactly 16 characters long.")
        return
        
    # Step 4: Convert to bytes
    pt_bytes = plaintext.encode('utf-8')
    key_bytes = key_input.encode('utf-8')
    
    modes = {
        'ECB': (AES.MODE_ECB, False),
        'CBC': (AES.MODE_CBC, True),
        'CFB': (AES.MODE_CFB, True),
        'OFB': (AES.MODE_OFB, True)
    }
    results = []
    print(f"\n{'-'*65}")
    print(f"{'Mode':<5} | {'Ciphertext (Hex)':<32} | {'Enc Time (s)':<10} | {'Dec Time (s)'}")
    print(f"{'-'*65}")
    
    for mode_name, (mode_val, requires_iv) in modes.items():
        # Step 6: Add padding
        padded_pt = pad(pt_bytes, AES.block_size)
        
        # Initialization Vector setup if required
        iv = get_random_bytes(AES.block_size) if requires_iv else None
        
        # Steps 5 & 7: Encrypt
        start_enc = time.perf_counter()
        cipher_enc = AES.new(key_bytes, mode_val, iv) if requires_iv else AES.new(key_bytes, mode_val)
        ciphertext = cipher_enc.encrypt(padded_pt)
        enc_time = time.perf_counter() - start_enc
        
        # Steps 9 & 10: Decrypt
        start_dec = time.perf_counter()
        cipher_dec = AES.new(key_bytes, mode_val, iv) if requires_iv else AES.new(key_bytes, mode_val)
        decrypted_padded = cipher_dec.decrypt(ciphertext)
        decrypted_pt = unpad(decrypted_padded, AES.block_size)
        dec_time = time.perf_counter() - start_dec
        
        # Step 8 & 11 data capture
        results.append({
            'mode': mode_name,
            'hex': ciphertext.hex()[:29] + "..." if len(ciphertext.hex()) > 32 else ciphertext.hex(),
            'decrypted': decrypted_pt.decode('utf-8')
        })
        print(f"{mode_name:<5} | {results[-1]['hex']:<32} | {enc_time:.6f}   | {dec_time:.6f}")

    # Verify decrypted outputs match original plaintext
    assert all(r['decrypted'] == plaintext for r in results), "Decryption verification failed."

    # Step 14 & 15: Compare security and performance characteristics
    print(f"\n{'-'*65}")
    print("Security and Performance Characteristics Comparison:")
    print(f"{'-'*65}")
    print("ECB has poor pattern security because identical plaintext blocks produce identical")
    print("ciphertext blocks. CBC, CFB, and OFB hide repeated plaintext patterns when IVs are")
    print("used correctly. Performance is compared experimentally using the measured")
    print("encryption and decryption execution times.")

if __name__ == "__main__":
    run_aes_experiment()