from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def main():
    print("--- AES-256 Symmetric Encryption ---")
    
    # 1. SETUP
    # Generate a random 32-byte (256-bit) secret key.
    # In the real world, you and the receiver must both securely hold this exact key.
    secret_key = get_random_bytes(32) 
    
    original_message = b"This is a highly confidential transmission."
    print(f"Original Message:  {original_message.decode('utf-8')}")

    # 2. ENCRYPTION
    # We use CBC (Cipher Block Chaining) mode. It requires an Initialization Vector (IV)
    # to ensure the same message doesn't produce the same ciphertext every time.
    cipher_encrypt = AES.new(secret_key, AES.MODE_CBC)
    iv = cipher_encrypt.iv 
    
    # AES encrypts in fixed blocks of 16 bytes. If our message isn't a perfect 
    # multiple of 16, 'pad' adds extra bytes to make it fit.
    padded_message = pad(original_message, AES.block_size)
    
    # Actually encrypt the data
    ciphertext = cipher_encrypt.encrypt(padded_message)
    print(f"Ciphertext (Hex):  {ciphertext.hex()}")

    # 3. DECRYPTION
    # To decrypt, we MUST have the exact same secret_key and the exact same IV.
    cipher_decrypt = AES.new(secret_key, AES.MODE_CBC, iv=iv)
    
    # Decrypt the data back to bytes
    decrypted_padded_message = cipher_decrypt.decrypt(ciphertext)
    
    # Remove the extra padding bytes we added earlier
    decrypted_message = unpad(decrypted_padded_message, AES.block_size)
    print(f"Decrypted Message: {decrypted_message.decode('utf-8')}")

if __name__ == "__main__":
    main()