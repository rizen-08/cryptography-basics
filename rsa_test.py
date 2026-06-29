from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def main():
    print("--- RSA Asymmetric Encryption ---")
    
    # 1. SETUP: Generate the Key Pair
    # 2048 bits is the standard minimum size for secure RSA keys today.
    # This generates two mathematically linked keys.
    key_pair = RSA.generate(2048)
    
    public_key = key_pair.publickey()
    private_key = key_pair
    
    original_message = b"Top secret: The eagle has landed."
    print(f"Original Message: {original_message.decode('utf-8')}\n")

    # 2. ENCRYPTION (Using the PUBLIC Key)
    # If a friend wants to send you a message, they use your Public Key.
    # PKCS1_OAEP is a standard padding scheme that makes RSA secure.
    cipher_rsa_encrypt = PKCS1_OAEP.new(public_key)
    
    # Encrypt the data. Note: RSA is mathematically heavy and can only 
    # encrypt very small amounts of data at a time!
    ciphertext = cipher_rsa_encrypt.encrypt(original_message)
    
    # The ciphertext is huge, so we will just print the first 60 characters
    print(f"Ciphertext (Hex): {ciphertext.hex()[:60]}... [Truncated]\n")

    # 3. DECRYPTION (Using the PRIVATE Key)
    # ONLY you hold the Private Key, so only you can read this message.
    cipher_rsa_decrypt = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa_decrypt.decrypt(ciphertext)
    
    print(f"Decrypted Message: {decrypted_message.decode('utf-8')}")

if __name__ == "__main__":
    main()